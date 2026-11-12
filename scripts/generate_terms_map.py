#!/usr/bin/env python3
import os
import re

WORKSPACE_DIR = "/home/ubermensch/Desktop/interview"

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

def clean_title(title):
    t = title.strip()
    t = re.sub(r"^\([^)]+\):\s*", "", t)
    t = re.sub(r"^[\"\']+|[\"\']+$", "", t)
    t = re.sub(r"^(What is the difference between|How do you|What is|What are|When should you|Why is|How does|What does|Explain|The differences between)\s+", "", t, flags=re.IGNORECASE)
    t = re.sub(r"\?$", "", t).strip()
    # truncate if excessively long
    if len(t) > 65:
        t = t[:62] + "..."
    return t[0].upper() + t[1:] if t else t

def extract_map():
    lines = []
    for fn in TARGET_FILES:
        path = os.path.join(WORKSPACE_DIR, fn)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        pattern = r"(^(?:##|###)\s+(?:Q[0-9]+|[0-9]+\.[0-9]+)[:\s]\s*([^\n]+))"
        splits = list(re.finditer(pattern, content, re.MULTILINE))
        
        for i, match in enumerate(splits):
            start = match.start()
            end = splits[i+1].start() if i+1 < len(splits) else len(content)
            block = content[start:end]
            raw_title = match.group(2).strip()
            q_title = clean_title(raw_title)

            terms_match = re.search(r"\*\*🎯 Terms[^\n]*\*\*(.*?)(?=\n\s*\n\s*\*\*|\Z)", block, re.DOTALL)
            star_terms = []
            if terms_match:
                for line in terms_match.group(1).split("\n"):
                    line = line.strip()
                    if ("⭐" in line or "★" in line) and (line.startswith("-") or line.startswith("*")):
                        line_content = re.sub(r"^[-*]\s+", "", line)
                        split_idx = -1
                        c_idx = line_content.find(":")
                        d_idx = line_content.find(" — ")
                        if c_idx != -1 and d_idx != -1:
                            split_idx = min(c_idx, d_idx)
                        elif c_idx != -1:
                            split_idx = c_idx
                        elif d_idx != -1:
                            split_idx = d_idx

                        term_part = line_content[:split_idx].strip() if split_idx != -1 else line_content.strip()
                        term_part = term_part.replace("⭐", "").replace("★", "").replace("**", "").strip()
                        if term_part:
                            star_terms.append(term_part)
            
            if star_terms:
                lines.append(f"| {q_title} | {', '.join(star_terms[:3])} |")
            else:
                lines.append(f"| {q_title} | (core terms pending) |")

    return lines

if __name__ == "__main__":
    entries = extract_map()
    print(f"Extracted {len(entries)} question-to-terms entries.")
    for e in entries[:10]:
        print(e)
