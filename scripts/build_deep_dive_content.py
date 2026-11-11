#!/usr/bin/env python3
"""
Full builder for 03_Angular_Signals_Deep_Dive.md adhering strictly to SSE-1.
"""
import os, sys

def format_q(num, title, companies, one_line, spoken, terms, hook, code, follow_up_q, follow_up_a, comparison=None, hood=None):
    comp_str = ", ".join(companies)
    lines = [
        f"## Q{num}: {title}",
        f"*Commonly asked at: {comp_str}*",
        "",
        "**⚡ One-line answer**",
        one_line.strip(),
        "",
        "**🗣️ Spoken answer (30–45 seconds)**",
        spoken.strip(),
        "",
        "**🎯 Terms the interviewer listens for**"
    ]
    for term, gloss, starred in terms:
        star = " ⭐" if starred else ""
        lines.append(f"- **{term}**: {gloss}{star}")
    lines.append("")
    lines.append("**🧠 Memory hook**")
    lines.append(hook.strip())
    lines.append("")
    lines.append("**💻 Code**")
    lines.append("```typescript")
    lines.append(code.strip())
    lines.append("```")
    lines.append("")
    lines.append("**⚠️ Likely follow-up**")
    lines.append(f"*Question:* {follow_up_q.strip()}")
    lines.append(f"*Answer:* {follow_up_a.strip()}")
    
    if comparison:
        lines.append("")
        lines.append("**📊 Quick comparison**")
        lines.append(comparison.strip())
        
    if hood:
        lines.append("")
        lines.append("**🔬 Under the hood (optional)**")
        lines.append(hood.strip())
        
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)
