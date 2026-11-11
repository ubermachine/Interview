#!/usr/bin/env python3
import sys, re, os

BANNED_STRINGS = [
    "battle-tested",
    "knockout",
    "gold standard",
    "mandatory senior default",
    "notorious",
    "catastrophic",
    "melts the database",
    "holy trinity",
    "90% of",
    "100% of"
]

BROKEN_LATEX = [
    "ightarrow",
    "$le$",
    "$ge$",
    "\\rightarrow",
    "\\ge",
    "\\le"
]

def check_banned(text, fname):
    errors = []
    lower_text = text.lower()
    for b in BANNED_STRINGS:
        if b in lower_text:
            for idx, line in enumerate(text.splitlines(), 1):
                if b in line.lower():
                    errors.append(f"{fname}:{idx}: Banned string found: '{b}'")
    for bl in BROKEN_LATEX:
        if bl in text:
            for idx, line in enumerate(text.splitlines(), 1):
                if bl in line:
                    errors.append(f"{fname}:{idx}: Broken LaTeX or LaTeX token found: '{bl}'")
    return errors

def count_words(s):
    cleaned = re.sub(r"[`*#_\[\]()\"']", " ", s)
    words = cleaned.split()
    return len(words)

def split_sentences(text):
    t = re.sub(r"\b(e\.g\.|i\.e\.|vs\.|etc\.)", "EG_TEMP", text)
    sents = [s.strip() for s in re.split(r"[.!?]+(?:\s+|$)", t) if s.strip()]
    return [s.replace("EG_TEMP", "e.g.") for s in sents]

def extract_section(block, header_title, next_headers):
    # Find header_title
    pattern = re.escape(header_title) + r"\s*\n+(.*?)(?=" + "|".join(re.escape(h) for h in next_headers) + r"|\Z)"
    m = re.search(pattern, block, re.DOTALL)
    if m:
        return m.group(1).strip()
    return None

def validate_question_block(q_num, block, fname):
    errors = []
    
    # 1. Commonly asked at
    asked_at_match = re.search(r"^\*Commonly asked at:\s*([^*]+)\*", block, re.MULTILINE)
    if not asked_at_match:
        errors.append(f"{fname} Q{q_num}: Missing '*Commonly asked at: <companies, max 4>*'")
    else:
        comps = [c.strip() for c in asked_at_match.group(1).split(",") if c.strip()]
        if len(comps) > 4:
            errors.append(f"{fname} Q{q_num}: More than 4 companies in commonly asked at: {len(comps)}")

    all_headers = [
        "**⚡ One-line answer**",
        "**🗣️ Spoken answer (30–45 seconds)**",
        "**🎯 Terms the interviewer listens for**",
        "**🧠 Memory hook**",
        "**💻 Code**",
        "**⚠️ Likely follow-up**",
        "**📊 Quick comparison**",
        "**🔬 Under the hood (optional)**",
        "## "
    ]

    # 2. One-line answer
    ola_text = extract_section(block, "**⚡ One-line answer**", all_headers[1:])
    if not ola_text:
        errors.append(f"{fname} Q{q_num}: Missing '**⚡ One-line answer**'")
    else:
        first_line = ola_text.splitlines()[0].strip()
        w_count = count_words(first_line)
        if w_count > 25:
            errors.append(f"{fname} Q{q_num}: One-line answer exceeds 25 words ({w_count} words): '{first_line}'")
        sents = split_sentences(first_line)
        if len(sents) > 1:
            errors.append(f"{fname} Q{q_num}: One-line answer must be 1 sentence (found {len(sents)}): '{first_line}'")

    # 3. Spoken answer
    sa_text = extract_section(block, "**🗣️ Spoken answer (30–45 seconds)**", all_headers[2:])
    if not sa_text:
        errors.append(f"{fname} Q{q_num}: Missing '**🗣️ Spoken answer (30–45 seconds)**'")
    else:
        sa_clean = re.sub(r"^>\s*", "", sa_text, flags=re.MULTILINE).strip()
        sa_joined = " ".join(sa_clean.split())
        w_count = count_words(sa_joined)
        if w_count < 60 or w_count > 90:
            errors.append(f"{fname} Q{q_num}: Spoken answer word count {w_count} not in [60, 90]")
        sents = split_sentences(sa_joined)
        if len(sents) < 4 or len(sents) > 6:
            errors.append(f"{fname} Q{q_num}: Spoken answer sentence count {len(sents)} not in [4, 6]")
        avg_w = w_count / len(sents) if sents else 0
        if avg_w > 15:
            errors.append(f"{fname} Q{q_num}: Spoken answer avg sentence word count {avg_w:.1f} > 15")
        for s in sents:
            sw = count_words(s)
            if sw > 25:
                errors.append(f"{fname} Q{q_num}: Spoken answer sentence exceeds 25 words ({sw}w): '{s[:40]}...'")

    # 4. Terms
    terms_text = extract_section(block, "**🎯 Terms the interviewer listens for**", all_headers[3:])
    if not terms_text:
        errors.append(f"{fname} Q{q_num}: Missing '**🎯 Terms the interviewer listens for**'")
    else:
        items = [line.strip() for line in terms_text.splitlines() if line.strip().startswith("-") or line.strip().startswith("*")]
        if len(items) < 5 or len(items) > 7:
            errors.append(f"{fname} Q{q_num}: Terms count {len(items)} not in [5, 7]")
        star_count = sum(1 for item in items if "⭐" in item)
        if star_count != 3:
            errors.append(f"{fname} Q{q_num}: Exactly 3 terms must have ⭐, found {star_count}")
        for item in items:
            m = re.search(r"\*\*(.+?)\*\*:\s*(.*)", item)
            if m:
                gloss = m.group(2).strip()
                gw = count_words(gloss)
                if gw > 10:
                    errors.append(f"{fname} Q{q_num}: Term '{m.group(1)}' gloss exceeds 10 words ({gw}w): '{gloss}'")
            else:
                errors.append(f"{fname} Q{q_num}: Term line does not match '- [⭐] **Term**: Gloss': '{item}'")

    # 5. Memory hook
    mh_text = extract_section(block, "**🧠 Memory hook**", all_headers[4:])
    if not mh_text:
        errors.append(f"{fname} Q{q_num}: Missing '**🧠 Memory hook**'")
    else:
        first_line = mh_text.splitlines()[0].strip()
        mw = count_words(first_line)
        if mw > 30:
            errors.append(f"{fname} Q{q_num}: Memory hook exceeds 30 words ({mw}w): '{first_line}'")

    # 6. Code
    code_text = extract_section(block, "**💻 Code**", all_headers[5:])
    if not code_text:
        errors.append(f"{fname} Q{q_num}: Missing '**💻 Code**'")
    else:
        m_cb = re.search(r"```[a-zA-Z]*\n(.*?)\n```", code_text, re.DOTALL)
        if not m_cb:
            errors.append(f"{fname} Q{q_num}: Code block missing or malformed")
        else:
            code = m_cb.group(1).strip()
            code_lines = [l for l in code.splitlines() if l.strip()]
            if len(code_lines) < 5 or len(code_lines) > 15:
                errors.append(f"{fname} Q{q_num}: Code lines {len(code_lines)} not in [5, 15]")
            has_cross = "❌" in code
            has_check = "✅" in code
            if not (has_cross and has_check):
                errors.append(f"{fname} Q{q_num}: Code must have one ❌/✅ pair")
            for cl in code.splitlines():
                if "//" in cl:
                    comment = cl.split("//", 1)[1].strip()
                    comment = comment.replace("❌", "").replace("✅", "").strip()
                    cw = count_words(comment)
                    if cw > 8:
                        errors.append(f"{fname} Q{q_num}: Code comment exceeds 8 words ({cw}w): '{comment}'")

    # 7. Likely follow-up
    fu_text = extract_section(block, "**⚠️ Likely follow-up**", all_headers[6:])
    if not fu_text:
        errors.append(f"{fname} Q{q_num}: Missing '**⚠️ Likely follow-up**'")
    else:
        q_m = re.search(r"\*?Q:\s*([^\n*]+)\*?", fu_text)
        a_m = re.search(r"\*?A:\s*([^\n]+(?:\n[^\n]+)*)", fu_text)
        if q_m:
            qw = count_words(q_m.group(1))
            if qw > 20:
                errors.append(f"{fname} Q{q_num}: Follow-up question exceeds 20 words ({qw}w)")
        else:
            errors.append(f"{fname} Q{q_num}: Missing 'Q: ...' in follow-up")
        if a_m:
            aw = count_words(a_m.group(1))
            if aw > 60:
                errors.append(f"{fname} Q{q_num}: Follow-up answer exceeds 60 words ({aw}w)")
        else:
            errors.append(f"{fname} Q{q_num}: Missing 'A: ...' in follow-up")

    # 8. Quick comparison
    qc_text = extract_section(block, "**📊 Quick comparison**", all_headers[7:])
    if not qc_text:
        errors.append(f"{fname} Q{q_num}: Missing '**📊 Quick comparison**'")
    else:
        tbl = [l.strip() for l in qc_text.splitlines() if l.strip().startswith("|")]
        if len(tbl) < 3:
            errors.append(f"{fname} Q{q_num}: Quick comparison table missing rows")
        else:
            data_rows = tbl[2:]
            if len(data_rows) > 5:
                errors.append(f"{fname} Q{q_num}: Quick comparison table has > 5 rows ({len(data_rows)})")
            for r in data_rows:
                cells = [c.strip() for c in r.split("|")[1:-1]]
                for c in cells:
                    cw = count_words(c)
                    if cw > 6:
                        errors.append(f"{fname} Q{q_num}: Comparison cell exceeds 6 words ({cw}w): '{c}'")

    # 9. Under the hood (optional)
    uth_text = extract_section(block, "**🔬 Under the hood (optional)**", all_headers[8:])
    if uth_text:
        uw = count_words(uth_text)
        if uw > 80:
            errors.append(f"{fname} Q{q_num}: Under the hood exceeds 80 words ({uw}w)")

    return errors

def validate_file(fname):
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    banned_errs = check_banned(content, fname)
    for be in banned_errs:
        print(f"BANNED: {be}")

    q_blocks = re.split(r"\n(?=## Q\d+:)", content)
    print(f"{fname}: Found {len(q_blocks)-1} Q blocks.")
    total_q_errs = 0
    for idx, b in enumerate(q_blocks[1:], 1):
        q_head = re.match(r"## Q(\d+):", b)
        q_num = q_head.group(1) if q_head else str(idx)
        errs = validate_question_block(q_num, b, fname)
        if errs:
            total_q_errs += len(errs)
            for e in errs:
                print(f"  ERROR: {e}")
    return len(banned_errs), total_q_errs

if __name__ == "__main__":
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        files = [
            "04_Microservices_Basic_Interview.md",
            "04_Microservices_Deep_Dive.md",
            "04_Microservices_SystemDesign.md",
            "05_Concurrency_Locks_Basic_Interview.md",
            "05_Concurrency_Locks_Deep_Dive.md",
            "05_Curated_Resources_Videos_Cheatsheet.md",
            "06_Concurrency_RaceConditions_EventDriven_Fixes.md",
            "06_Security_DevOps_Basic_Interview.md",
            "06_Security_DevOps_Deep_Dive.md",
            "07_Security_Testing_DevOps_AdjacentSkills.md"
        ]
    for f in files:
        if os.path.exists(f):
            validate_file(f)
