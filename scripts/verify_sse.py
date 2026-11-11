#!/usr/bin/env python3
import sys, os, re

BANNED_WORDS = [
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

def split_sentences(text):
    text = text.strip()
    clean = text
    clean = re.sub(r'\b(e\.g\.|i\.e\.|vs\.|etc\.)', lambda m: m.group(1).replace('.', '@'), clean, flags=re.I)
    raw_s = re.split(r'(?<=[.!?])\s+', clean)
    sentences = [s.replace('@', '.').strip() for s in raw_s if s.strip()]
    return sentences

def count_words(text):
    cleaned = re.sub(r'[*_`#\[\]]', ' ', text)
    tokens = [t for t in cleaned.split() if t]
    return len(tokens)

def check_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []
    
    # Check banned words in entire file
    for bw in BANNED_WORDS:
        matches = [m.start() for m in re.finditer(r'\b' + re.escape(bw) + r'\b', content, re.IGNORECASE)]
        if matches:
            errors.append(f"Found banned word '{bw}' {len(matches)} time(s) in file.")

    # Split into questions by '## '
    sections = re.split(r'\n(?=## )', content)
    questions = [s for s in sections if s.startswith('## ')]

    print(f"Total question sections found: {len(questions)}")

    for idx, q_text in enumerate(questions):
        lines = q_text.strip().split('\n')
        q_heading = lines[0].strip()
        q_name = q_heading[:50]

        # 1. Heading check
        if not re.match(r'^## (Q\d+|1\.\d+):', q_heading):
            errors.append(f"[{q_name}] Heading does not match '## Q<n>:' or '## 1.<n>:'")

        # 2. Commonly asked at check
        asked_match = re.search(r'\*Commonly asked at:\s*([^*]+)\*', q_text)
        if not asked_match:
            errors.append(f"[{q_name}] Missing '*Commonly asked at: <companies>*'")
        else:
            companies = [c.strip() for c in asked_match.group(1).split(',') if c.strip()]
            if len(companies) > 4:
                errors.append(f"[{q_name}] Too many companies: {len(companies)} (max 4)")

        # 3. One-line answer
        one_line_match = re.search(r'\*\*⚡ One-line answer\*\*\s*\n+(.*?)(?=\n\*\*|\n---|\Z)', q_text, re.DOTALL)
        if not one_line_match:
            errors.append(f"[{q_name}] Missing '**⚡ One-line answer**'")
        else:
            ans = one_line_match.group(1).strip()
            wc = count_words(ans)
            if wc > 25:
                errors.append(f"[{q_name}] One-line answer exceeds 25 words ({wc} words)")
            s_list = split_sentences(ans)
            if len(s_list) != 1:
                errors.append(f"[{q_name}] One-line answer must be 1 sentence, got {len(s_list)}")

        # 4. Spoken answer
        spoken_match = re.search(r'\*\*🗣️ Spoken answer \(30–45 seconds\)\*\*\s*\n+(.*?)(?=\n\*\*|\n---|\Z)', q_text, re.DOTALL)
        if not spoken_match:
            errors.append(f"[{q_name}] Missing '**🗣️ Spoken answer (30–45 seconds)**'")
        else:
            spoken_text = spoken_match.group(1).strip()
            wc = count_words(spoken_text)
            if wc < 60 or wc > 90:
                errors.append(f"[{q_name}] Spoken answer words not in 60-90: got {wc} words")
            sentences = split_sentences(spoken_text)
            if len(sentences) < 4 or len(sentences) > 6:
                errors.append(f"[{q_name}] Spoken answer sentence count not in 4-6: got {len(sentences)}")
            if sentences:
                avg_len = sum(count_words(s) for s in sentences) / len(sentences)
                if avg_len > 15.01:
                    errors.append(f"[{q_name}] Spoken answer avg sentence length > 15w: {avg_len:.1f}")
                for s in sentences:
                    swc = count_words(s)
                    if swc > 25:
                        errors.append(f"[{q_name}] Spoken answer sentence exceeds 25w ({swc}w): '{s[:40]}...'")

        # 5. Terms the interviewer listens for
        terms_match = re.search(r'\*\*🎯 Terms the interviewer listens for\*\*\s*\n((?:- .*\n?)+)', q_text)
        if not terms_match:
            errors.append(f"[{q_name}] Missing '**🎯 Terms the interviewer listens for**'")
        else:
            terms_lines = [l.strip() for l in terms_match.group(1).strip().split('\n') if l.strip().startswith('-')]
            if len(terms_lines) < 5 or len(terms_lines) > 7:
                errors.append(f"[{q_name}] Terms count not in 5-7: got {len(terms_lines)}")
            star_count = sum(1 for l in terms_lines if '⭐' in l)
            if star_count != 3:
                errors.append(f"[{q_name}] Marked with ⭐ count is not 3: got {star_count}")
            for tl in terms_lines:
                parts = tl.split(':', 1)
                if len(parts) == 2:
                    gloss = parts[1].strip()
                    g_words = count_words(gloss)
                    if g_words > 10:
                        errors.append(f"[{q_name}] Term gloss > 10w ({g_words}w): '{tl[:50]}'")

        # 6. Memory hook
        hook_match = re.search(r'\*\*🧠 Memory hook\*\*\s*\n+(.*?)(?=\n\*\*|\n---|\Z)', q_text, re.DOTALL)
        if not hook_match:
            errors.append(f"[{q_name}] Missing '**🧠 Memory hook**'")
        else:
            hook_text = hook_match.group(1).strip()
            hwc = count_words(hook_text)
            if hwc > 30:
                errors.append(f"[{q_name}] Memory hook exceeds 30 words ({hwc}w)")

        # 7. Code
        code_match = re.search(r'```(?:csharp|sql|xml|bash)?\n(.*?)```', q_text, re.DOTALL)
        if not code_match:
            errors.append(f"[{q_name}] Missing code block")
        else:
            code_lines = [l for l in code_match.group(1).split('\n') if l.strip()]
            if len(code_lines) < 5 or len(code_lines) > 15:
                errors.append(f"[{q_name}] Code lines not in 5-15: got {len(code_lines)}")
            code_str = code_match.group(1)
            if ('❌' not in code_str) or ('✅' not in code_str):
                errors.append(f"[{q_name}] Code block missing ❌/✅ pair")
            for cl in code_lines:
                if '//' in cl:
                    comment = cl.split('//', 1)[1].strip()
                    cwc = count_words(comment)
                    if cwc > 8:
                        errors.append(f"[{q_name}] Code comment > 8 words ({cwc}w): '// {comment}'")
                elif '--' in cl:
                    comment = cl.split('--', 1)[1].strip()
                    cwc = count_words(comment)
                    if cwc > 8:
                        errors.append(f"[{q_name}] Code comment > 8 words ({cwc}w): '-- {comment}'")

        # 8. Likely follow-up
        follow_match = re.search(r'\*\*⚠️ Likely follow-up\*\*\s*\n+(.*?)(?=\n\*\*📊 Quick comparison\*\*|\n---|\Z)', q_text, re.DOTALL)
        if not follow_match:
            errors.append(f"[{q_name}] Missing '**⚠️ Likely follow-up**'")
        else:
            f_text = follow_match.group(1).strip()
            q_m = re.search(r'(?:\*\*|\*)?(?:Q|Question)(?:\*\*|\*)?:\s*(.+?)(?=\n(?:\*\*|\*)?(?:A|Answer)(?:\*\*|\*)?:|\Z)', f_text, re.DOTALL | re.I)
            a_m = re.search(r'(?:\*\*|\*)?(?:A|Answer)(?:\*\*|\*)?:\s*(.+)', f_text, re.DOTALL | re.I)
            if q_m and a_m:
                fq = q_m.group(1).strip()
                fa = a_m.group(1).strip()
                fq_words = count_words(fq)
                fa_words = count_words(fa)
                if fq_words > 20:
                    errors.append(f"[{q_name}] Follow-up Q > 20 words ({fq_words}w): '{fq[:40]}'")
                if fa_words > 60:
                    errors.append(f"[{q_name}] Follow-up A > 60 words ({fa_words}w): '{fa[:40]}'")
            else:
                errors.append(f"[{q_name}] Follow-up missing structured Q/A format")

        # 9. Quick comparison
        table_match = re.search(r'(\|.+?\|\n\|[-:| ]+\|\n(?:\|.+?\|\n?)+)', q_text)
        if not table_match:
            errors.append(f"[{q_name}] Missing '**📊 Quick comparison**' table")
        else:
            tbl_lines = [l.strip() for l in table_match.group(1).strip().split('\n') if l.strip()]
            data_rows = tbl_lines[2:]
            if len(data_rows) > 5:
                errors.append(f"[{q_name}] Quick comparison table has > 5 data rows ({len(data_rows)} rows)")
            for r in data_rows:
                cells = [c.strip() for c in r.strip('|').split('|')]
                for cell in cells:
                    cell_wc = count_words(cell)
                    if cell_wc > 6:
                        errors.append(f"[{q_name}] Table cell > 6 words ({cell_wc}w): '{cell}'")

        # 10. Under the hood (optional)
        uth_match = re.search(r'\*\*🔬 Under the hood\*\*\s*\n+(.*?)(?=\n\*\*|\n---|\Z)', q_text, re.DOTALL)
        if uth_match:
            uth_text = uth_match.group(1).strip()
            uwc = count_words(uth_text)
            if uwc > 80:
                errors.append(f"[{q_name}] Under the hood exceeds 80 words ({uwc}w)")

    print(f"Total validation errors: {len(errors)}")
    for e in errors[:30]:
        print("  -", e)
    if len(errors) > 30:
        print(f"  ... and {len(errors) - 30} more")
    return len(errors) == 0

if __name__ == '__main__':
    fpath = sys.argv[1] if len(sys.argv) > 1 else "01_DotNet_Core_Basic_Interview.md"
    success = check_file(fpath)
    sys.exit(0 if success else 1)
