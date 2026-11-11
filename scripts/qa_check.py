#!/usr/bin/env python3
import glob, os, re, sys

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BANNED_PATTERNS = [
    (r'(?i)\bbattle-tested\b', 'battle-tested'),
    (r'(?i)\bknockout\b', 'knockout'),
    (r'(?i)\bgold standard\b', 'gold standard'),
    (r'(?i)\bmandatory senior default\b', 'mandatory senior default'),
    (r'(?i)\bnotorious\b', 'notorious'),
    (r'(?i)\bholy trinity\b', 'holy trinity'),
    (r'(?i)\bmelts the database\b', 'melts the database'),
    (r'(?i)literally\s+100%', 'literally 100%'),
    (r'(?i)asked in\s+(?:90%|100%)', 'fake percentages (asked in 90%/100%)'),
    (r'(?i)\bcartographic\b', 'cartographic (invented term)'),
    (r'(?i)\bIL Weaving\b', 'IL Weaving (for EF lazy loading - should be Castle DynamicProxy)'),
    (r'(?i)"In our (?:Morgan Stanley|JPMorgan|Wells Fargo|Goldman Sachs|Barclays)\b', 'fabricated employer quote'),
    (r'\$\s*\\rightarrow\s*\$', '$\\rightarrow$ broken LaTeX'),
    (r'\$\s*ightarrow\s*\$', '$ ightarrow$ broken LaTeX'),
    (r'\$\s*le\s*\d*\s*\$', '$le$ broken LaTeX'),
    (r'\$\s*ge\s*\d*\s*\$', '$ge$ broken LaTeX'),
    (r'\$\s*M\s+imes\s+N\s*\$', '$M imes N$ broken LaTeX'),
    (r'[⋈⊎]', 'relational algebra symbol in markdown'),
]

def check_files():
    total_violations = 0
    md_files = sorted(glob.glob(os.path.join(WORKSPACE_DIR, '*.md')))
    
    print(f"Scanning {len(md_files)} markdown files for QA violations...")
    
    for fpath in md_files:
        fname = os.path.basename(fpath)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines()

        file_violations = []
        for line_idx, line in enumerate(lines, 1):
            for pattern, name in BANNED_PATTERNS:
                if re.search(pattern, line):
                    file_violations.append((line_idx, name, line.strip()[:100]))

        if file_violations:
            print(f"\n❌ {fname} has {len(file_violations)} violation(s):")
            for lno, vname, sample in file_violations[:10]:
                print(f"   L{lno}: [{vname}] {sample}")
            if len(file_violations) > 10:
                print(f"   ... and {len(file_violations) - 10} more.")
            total_violations += len(file_violations)
        else:
            print(f"✅ {fname}: clean")

    print(f"\n==========================================")
    if total_violations == 0:
        print("🎉 ALL QA CHECKS PASSED WITH ZERO VIOLATIONS!")
        return 0
    else:
        print(f"⚠️ TOTAL VIOLATIONS DETECTED: {total_violations}")
        return 1

if __name__ == '__main__':
    sys.exit(check_files())
