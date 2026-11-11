#!/usr/bin/env python3
import re, sys, os

def count_words(text):
    # remove markdown formatting and code
    clean = re.sub(r'[`*_#\[\]\(\)]', ' ', text)
    tokens = clean.strip().split()
    return len(tokens)

def split_sentences(text):
    # split text by sentence-ending punctuation . ! ? but ignore numbers like v16.2 or e.g. or vs.
    text = re.sub(r'\b(e\.g\.|i\.e\.|vs\.|Dr\.|Mr\.|Mrs\.)', lambda m: m.group(0).replace('.', '@'), text)
    text = re.sub(r'(\d+)\.(\d+)', r'\1@\2', text)
    sentences = [s.strip().replace('@', '.') for s in re.split(r'[.!?]+(?:\s+|$)', text) if s.strip()]
    return sentences

BANNED_STRINGS = [
    (r'\bbattle-tested\b', 'battle-tested'),
    (r'\bknockout\b', 'knockout'),
    (r'\bgold standard\b', 'gold standard'),
    (r'\bmandatory senior default\b', 'mandatory senior default'),
    (r'\bnotorious\b', 'notorious'),
    (r'\bcatastrophic\b', 'catastrophic'),
    (r'\bholy trinity\b', 'holy trinity'),
    (r'90%\s+of', '90% of'),
    (r'100%\s+of', '100% of'),
    (r'literally\s+100%', 'literally 100%'),
    (r'melts the database', 'melts the database'),
    (r'\bcartographic\b', 'cartographic'),
    (r'\bIL Weaving\b', 'IL Weaving'),
    (r'In our (?:Morgan Stanley|JPMorgan|Wells Fargo|Goldman Sachs|Barclays|Flipkart|Swiggy)', 'Fabricated employer quote'),
    (r'ES6 Proxies', 'SignalStore ES6 Proxies myth'),
    (r'O\(1\) memoiz', 'SignalStore O(1) memoization myth'),
    (r'\$\s*\\rightarrow\s*\$', '$\\rightarrow$ broken LaTeX'),
    (r'\$\s*le\s*\d*\s*\$', '$le$ broken LaTeX'),
    (r'\$\s*ge\s*\d*\s*\$', '$ge$ broken LaTeX'),
]

def check_question(q_num, q_title, q_body):
    errors = []
    
    # 1. Check Commonly asked at
    asked_match = re.search(r'\*Commonly asked at:\s*([^*]+)\*', q_body)
    if not asked_match:
        errors.append("Missing '*Commonly asked at: <companies, max 4>*'")
    else:
        companies = [c.strip() for c in asked_match.group(1).split(',') if c.strip()]
        if len(companies) > 4:
            errors.append(f"Too many companies ({len(companies)} > 4) in Commonly asked at")

    # 2. Check One-line answer
    one_line_match = re.search(r'\*\*⚡ One-line answer\*\*\s*\n+([^\n*]+)', q_body)
    if not one_line_match:
        errors.append("Missing '**⚡ One-line answer**'")
    else:
        text = one_line_match.group(1).strip()
        wc = count_words(text)
        if wc > 25:
            errors.append(f"One-line answer exceeds 25 words ({wc} words): '{text}'")
        sents = split_sentences(text)
        if len(sents) != 1:
            errors.append(f"One-line answer should be exactly 1 sentence, got {len(sents)}")

    # 3. Check Spoken answer
    spoken_match = re.search(r'\*\*🗣️ Spoken answer \(30–45 seconds\)\*\*\s*\n+((?:[^\n*#]|(?!\*\*)[^\n#])+(?:\n+(?:[^\n*#]|(?!\*\*)[^\n#])+)*)', q_body)
    if not spoken_match:
        errors.append("Missing '**🗣️ Spoken answer (30–45 seconds)**'")
    else:
        spoken_raw = spoken_match.group(1).strip()
        # Clean blockquotes if present
        spoken_clean = re.sub(r'^\s*>\s*', '', spoken_raw, flags=re.MULTILINE).strip()
        wc = count_words(spoken_clean)
        if wc < 60 or wc > 90:
            errors.append(f"Spoken answer word count {wc} outside 60-90 words range")
        sents = split_sentences(spoken_clean)
        if len(sents) < 4 or len(sents) > 6:
            errors.append(f"Spoken answer sentence count {len(sents)} outside 4-6 range")
        if sents:
            avg_w = sum(count_words(s) for s in sents) / len(sents)
            if avg_w > 15.5:
                errors.append(f"Spoken answer avg sentence length {avg_w:.1f} > 15 words")
            for s in sents:
                swc = count_words(s)
                if swc > 25:
                    errors.append(f"Spoken answer sentence exceeds 25 words ({swc}w): '{s[:40]}...'")

    # 4. Check Terms
    terms_match = re.search(r'\*\*🎯 Terms the interviewer listens for\*\*\s*\n+((?:\s*-\s*[^\n]+\n*)+)', q_body)
    if not terms_match:
        errors.append("Missing '**🎯 Terms the interviewer listens for**'")
    else:
        term_lines = [line.strip() for line in terms_match.group(1).strip().splitlines() if line.strip().startswith('-')]
        if len(term_lines) < 5 or len(term_lines) > 7:
            errors.append(f"Terms count {len(term_lines)} outside 5-7 range")
        star_count = sum(1 for line in term_lines if '⭐' in line)
        if star_count != 3:
            errors.append(f"Terms with ⭐ should be exactly 3, got {star_count}")
        for t in term_lines:
            # check gloss length: - **Term**: gloss ⭐
            gloss_match = re.search(r'-\s*\*\*([^*]+)\*\*:\s*([^⭐\n]+)', t)
            if gloss_match:
                gloss = gloss_match.group(2).strip()
                if count_words(gloss) > 10:
                    errors.append(f"Term gloss exceeds 10 words ({count_words(gloss)}w): '{gloss}'")

    # 5. Check Memory hook
    hook_match = re.search(r'\*\*🧠 Memory hook\*\*\s*\n+([^\n*#]+)', q_body)
    if not hook_match:
        errors.append("Missing '**🧠 Memory hook**'")
    else:
        hook_text = hook_match.group(1).strip()
        wc = count_words(hook_text)
        if wc > 30:
            errors.append(f"Memory hook exceeds 30 words ({wc} words): '{hook_text}'")

    # 6. Check Code
    code_match = re.search(r'\*\*💻 Code\*\*\s*\n+```[a-z]*\n(.*?)```', q_body, re.DOTALL)
    if not code_match:
        errors.append("Missing '**💻 Code**' block")
    else:
        code_lines = [l for l in code_match.group(1).strip().splitlines() if l.strip()]
        if len(code_lines) < 5 or len(code_lines) > 15:
            errors.append(f"Code lines count {len(code_lines)} outside 5-15 range")
        code_str = code_match.group(1)
        if '❌' not in code_str or '✅' not in code_str:
            errors.append("Code missing ❌ / ✅ pair")
        # Check comment length
        for l in code_lines:
            c_match = re.search(r'//\s*([^\n]+)', l)
            if c_match:
                c_text = c_match.group(1).strip()
                # remove ❌ or ✅ emoji
                c_clean = c_text.replace('❌', '').replace('✅', '').strip()
                if count_words(c_clean) > 8:
                    errors.append(f"Code comment exceeds 8 words ({count_words(c_clean)}w): '{c_text}'")

    # 7. Check Likely follow-up
    followup_match = re.search(r'\*\*⚠️ Likely follow-up\*\*\s*\n+(.*?)(?=\n\s*\*\*|\n\s*##|\n\s*---|\Z)', q_body, re.DOTALL)
    if not followup_match:
        errors.append("Missing '**⚠️ Likely follow-up**'")
    else:
        f_text = followup_match.group(1).strip()
        q_m = re.search(r'\*(?:Question|Follow-up):\*\s*([^\n*]+)', f_text)
        a_m = re.search(r'\*Answer:\*\s*(.+)', f_text, re.DOTALL)
        if not q_m or not a_m:
            errors.append("Likely follow-up missing *Question:* or *Answer:*")
        else:
            q_wc = count_words(q_m.group(1).strip())
            a_wc = count_words(a_m.group(1).strip())
            if q_wc > 20:
                errors.append(f"Follow-up question exceeds 20 words ({q_wc}w)")
            if a_wc > 60:
                errors.append(f"Follow-up answer exceeds 60 words ({a_wc}w)")

    # 8. Check Quick comparison (if present)
    comp_match = re.search(r'\*\*📊 Quick comparison\*\*\s*\n+(\|.*?\n\|.*?\n(?:\|.*?\n)+)', q_body)
    if comp_match:
        table_lines = [l.strip() for l in comp_match.group(1).strip().splitlines() if l.strip()]
        data_rows = [l for l in table_lines[2:] if l.startswith('|')]
        if len(data_rows) > 5:
            errors.append(f"Quick comparison table has > 5 rows ({len(data_rows)} rows)")
        for r in data_rows:
            cells = [c.strip() for c in r.split('|')[1:-1]]
            for c in cells:
                if count_words(c) > 6:
                    errors.append(f"Comparison cell exceeds 6 words ({count_words(c)}w): '{c}'")

    # 9. Check Under the hood (if present)
    hood_match = re.search(r'\*\*🔬 Under the hood(?: \(optional\))?\*\*\s*\n+([^\n#]+(?:\n+[^\n#]+)*)', q_body)
    if hood_match:
        h_text = hood_match.group(1).strip()
        # stop before next section or separator
        h_text = re.split(r'\n\s*---|\n\s*##|\n\s*\*\*', h_text)[0].strip()
        h_wc = count_words(h_text)
        if h_wc > 80:
            errors.append(f"Under the hood exceeds 80 words ({h_wc}w)")

    # 10. Check Banned strings
    for pattern, name in BANNED_STRINGS:
        if re.search(pattern, q_body, re.IGNORECASE):
            errors.append(f"Contains banned pattern: {name}")

    return errors

def validate_file(filepath):
    print(f"\n==================================================")
    print(f"Validating {os.path.basename(filepath)}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all questions: ## Q<n>: <title>
    q_matches = list(re.finditer(r'^##\s+(Q\d+:\s*[^\n]+)', content, re.MULTILINE))
    if not q_matches:
        print(f"❌ No '## Q<n>:' headings found in {filepath}!")
        return 1

    print(f"Found {len(q_matches)} questions.")
    total_q_errors = 0
    for i, m in enumerate(q_matches):
        q_heading = m.group(1)
        start_idx = m.end()
        end_idx = q_matches[i+1].start() if i+1 < len(q_matches) else len(content)
        q_body = content[start_idx:end_idx]
        
        # We also want to exclude trailing non-question sections if this is the last question
        # like '--- \n # ADVANCED ...'
        if i == len(q_matches) - 1:
            q_body = re.split(r'\n#+\s+', q_body)[0]

        errors = check_question(i+1, q_heading, q_body)
        if errors:
            print(f"\n❌ {q_heading.splitlines()[0]}:")
            for err in errors:
                print(f"   - {err}")
            total_q_errors += len(errors)

    if total_q_errors == 0:
        print(f"✅ All {len(q_matches)} questions in {os.path.basename(filepath)} passed validation!")
        return 0
    else:
        print(f"⚠️ {os.path.basename(filepath)} has {total_q_errors} question violation(s)!")
        return 1

if __name__ == '__main__':
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        files = [
            '/home/ubermensch/Desktop/interview/03_Angular_Signals_Basic_Interview.md',
            '/home/ubermensch/Desktop/interview/03_Angular_Signals_Deep_Dive.md',
            '/home/ubermensch/Desktop/interview/03_Angular_Signals_RxJS.md'
        ]
    exit_code = 0
    for f in files:
        if validate_file(f) != 0:
            exit_code = 1
    sys.exit(exit_code)
