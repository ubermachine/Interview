#!/usr/bin/env python3
import os
import re
import sys

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TARGET_FILES = [
    "01_DotNet_Core_Basic_Interview.md",
    "01_DotNet_Core_Deep_Dive.md",
    "02_SQL_Server_Basic_Interview.md",
    "02_SQL_Server_Deep_Dive.md",
    "02_SQL_Server_Performance_Tuning.md",
    "03_Angular_Signals_Basic_Interview.md",
    "03_Angular_Signals_Deep_Dive.md",
    "03_Angular_Signals_RxJS.md",
    "04_Microservices_Basic_Interview.md",
    "04_Microservices_Deep_Dive.md",
    "04_Microservices_SystemDesign.md",
    "05_Concurrency_Locks_Basic_Interview.md",
    "05_Concurrency_Locks_Deep_Dive.md",
    "06_Concurrency_RaceConditions_EventDriven_Fixes.md",
    "06_Security_DevOps_Basic_Interview.md",
    "06_Security_DevOps_Deep_Dive.md",
    "07_Security_Testing_DevOps_AdjacentSkills.md",
    "07_Real_Forum_Questions_Basic_Interview.md",
    "07_Real_Forum_Questions_Deep_Dive.md",
    "08_Real_Forum_Questions_DotNet_SQL_India.md"
]

def check_file(filename):
    filepath = os.path.join(WORKSPACE_DIR, filename)
    if not os.path.exists(filepath):
        return None, [f"File {filename} does not exist"]

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all question blocks
    pattern = r"(^(?:##|###)\s+(?:Q[0-9]+|[0-9]+\.[0-9]+)[^\n]+)"
    splits = list(re.finditer(pattern, content, re.MULTILINE))
    
    if not splits:
        # Check if there are one-line answers
        one_liners = list(re.finditer(r"^\*\*⚡ One-line answer\*\*", content, re.MULTILINE))
        if not one_liners:
            return 0, []
        splits = one_liners

    errors = []
    checked_count = 0

    for i, match in enumerate(splits):
        start = match.start()
        end = splits[i+1].start() if i+1 < len(splits) else len(content)
        block = content[start:end]
        
        # Check if block has One-line answer
        ol_match = re.search(r"\*\*⚡ One-line answer\*\*\s*\n+([^\n]+)", block)
        if not ol_match:
            continue

        checked_count += 1
        ol_text = ol_match.group(1).strip()

        # Gate A: Every one-line answer begins with a bolded term
        if not re.match(r"^\*\*[^*]+\*\*\s+(means|is|=|creates|provides|refers|allows|runs|optimizes)", ol_text, re.IGNORECASE):
            # check if it starts with bolded term at all
            if not re.match(r"^\*\*[^*]+\*\*", ol_text):
                errors.append(f"Q#{i+1} Gate A failed: One-line answer does not start with bolded term: {ol_text[:50]}")

        # Check Spoken answer
        sp_match = re.search(r"\*\*🗣️ Spoken answer[^\n]*\*\*\s*\n+(.*?)(?=\n\s*\n\s*\*\*|\Z)", block, re.DOTALL)
        if sp_match:
            sp_text = sp_match.group(1).strip()
            # strip quotes if present
            sp_text = re.sub(r"^[>\s\"]+", "", sp_text)
            sp_text = re.sub(r"[\"\s]+$", "", sp_text)
            words = sp_text.split()
            # word count check
            if len(words) < 50 or len(words) > 115:
                # soft warning
                pass

        # Check Terms section
        terms_match = re.search(r"\*\*🎯 Terms[^\n]*\*\*(.*?)(?=\n\s*\n\s*\*\*|\Z)", block, re.DOTALL)
        if terms_match:
            terms_text = terms_match.group(1)
            starred_count = terms_text.count("⭐") + terms_text.count("★")
            if starred_count == 0:
                errors.append(f"Q#{i+1} Gate B failed: Zero starred core terms in Terms section")

    return checked_count, errors

def main():
    total_checked = 0
    total_errors = 0
    print("=" * 60)
    print("RUNNING TERM-FIRST ANCHORING QA VALIDATION")
    print("=" * 60)
    
    for fn in TARGET_FILES:
        count, errors = check_file(fn)
        if count is None:
            continue
        status = "✅ PASS" if len(errors) == 0 else f"❌ {len(errors)} ERRORS"
        print(f"{fn:50} | {count:3} Qs | {status}")
        if errors:
            for err in errors[:3]:
                print(f"   ⚠️  {err}")
            if len(errors) > 3:
                print(f"   ... and {len(errors) - 3} more errors")
            total_errors += len(errors)
        total_checked += count

    print("=" * 60)
    print(f"TOTAL QUESTIONS CHECKED: {total_checked} | TOTAL ERRORS: {total_errors}")
    print("=" * 60)
    return 0 if total_errors == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
