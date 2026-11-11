#!/usr/bin/env python3
import os, json, re, sys

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTAL_FILE = os.path.join(WORKSPACE_DIR, 'Study_Portal.html')

manifest = [
    {
        "id": "01_DotNet_Core_Basic_Interview",
        "filename": "01_DotNet_Core_Basic_Interview.md",
        "title": "01. .NET Core & C# (Basic Interview)",
        "badge": "🟢 Basic Q&A",
        "type": "basic",
        "icon": "⚡",
        "domain": "01. .NET Core & C# Internals"
    },
    {
        "id": "01_DotNet_Core_Deep_Dive",
        "filename": "01_DotNet_Core_Deep_Dive.md",
        "title": "01. .NET Core & C# (Indian Senior Rounds)",
        "badge": "🇮🇳 Indian Hitlist",
        "type": "deep",
        "icon": "⚡",
        "domain": "01. .NET Core & C# Internals"
    },
    {
        "id": "02_SQL_Server_Basic_Interview",
        "filename": "02_SQL_Server_Basic_Interview.md",
        "title": "02. SQL Server Tuning (Basic Interview)",
        "badge": "🟢 Basic Q&A",
        "type": "basic",
        "icon": "🗄️",
        "domain": "02. SQL Server & Performance Tuning"
    },
    {
        "id": "02_SQL_Server_Deep_Dive",
        "filename": "02_SQL_Server_Deep_Dive.md",
        "title": "02. SQL Server Tuning (Deep Dive)",
        "badge": "🟣 Deep Dive",
        "type": "deep",
        "icon": "🗄️",
        "domain": "02. SQL Server & Performance Tuning"
    },
    {
        "id": "03_Angular_Signals_Basic_Interview",
        "filename": "03_Angular_Signals_Basic_Interview.md",
        "title": "03. Angular & Signals (Basic Interview)",
        "badge": "🟢 Basic Q&A",
        "type": "basic",
        "icon": "🅰️",
        "domain": "03. Angular 17/18 & Signals"
    },
    {
        "id": "03_Angular_Signals_Deep_Dive",
        "filename": "03_Angular_Signals_Deep_Dive.md",
        "title": "03. Angular & Signals (Deep Dive)",
        "badge": "🟣 Deep Dive",
        "type": "deep",
        "icon": "🅰️",
        "domain": "03. Angular 17/18 & Signals"
    },
    {
        "id": "04_Microservices_Basic_Interview",
        "filename": "04_Microservices_Basic_Interview.md",
        "title": "04. Microservices (Basic Interview)",
        "badge": "🟢 Basic Q&A",
        "type": "basic",
        "icon": "🌐",
        "domain": "04. Microservices & Distributed Systems"
    },
    {
        "id": "04_Microservices_Deep_Dive",
        "filename": "04_Microservices_Deep_Dive.md",
        "title": "04. Microservices (Deep Dive)",
        "badge": "🟣 Deep Dive",
        "type": "deep",
        "icon": "🌐",
        "domain": "04. Microservices & Distributed Systems"
    },
    {
        "id": "05_Concurrency_Locks_Basic_Interview",
        "filename": "05_Concurrency_Locks_Basic_Interview.md",
        "title": "05. Concurrency & Locks (Basic Interview)",
        "badge": "🟢 Basic Q&A",
        "type": "basic",
        "icon": "🔒",
        "domain": "05. Concurrency & Race Conditions"
    },
    {
        "id": "05_Concurrency_Locks_Deep_Dive",
        "filename": "05_Concurrency_Locks_Deep_Dive.md",
        "title": "05. Concurrency & Locks (Deep Dive)",
        "badge": "🟣 Deep Dive",
        "type": "deep",
        "icon": "🔒",
        "domain": "05. Concurrency & Race Conditions"
    },
    {
        "id": "06_Security_DevOps_Basic_Interview",
        "filename": "06_Security_DevOps_Basic_Interview.md",
        "title": "06. Security & DevOps (Basic Interview)",
        "badge": "🟢 Basic Q&A",
        "type": "basic",
        "icon": "🛡️",
        "domain": "06. Security, Testing & DevOps"
    },
    {
        "id": "06_Security_DevOps_Deep_Dive",
        "filename": "06_Security_DevOps_Deep_Dive.md",
        "title": "06. Security & DevOps (Deep Dive)",
        "badge": "🟣 Deep Dive",
        "type": "deep",
        "icon": "🛡️",
        "domain": "06. Security, Testing & DevOps"
    },
    {
        "id": "07_Real_Forum_Questions_Basic_Interview",
        "filename": "07_Real_Forum_Questions_Basic_Interview.md",
        "title": "07. Real Forum Qs (Basic Interview)",
        "badge": "🟢 Basic Q&A",
        "type": "basic",
        "icon": "💬",
        "domain": "07. Forum & Production War Stories"
    },
    {
        "id": "07_Real_Forum_Questions_Deep_Dive",
        "filename": "07_Real_Forum_Questions_Deep_Dive.md",
        "title": "07. Real Forum Qs (Deep Dive)",
        "badge": "🟣 Deep Dive",
        "type": "deep",
        "icon": "💬",
        "domain": "07. Forum & Production War Stories"
    },
    {
        "id": "08_Master_Cheatsheet_Quick_Ref",
        "filename": "08_Master_Cheatsheet_Quick_Ref.md",
        "title": "08. Master Cheatsheet & Formulas",
        "badge": "⚡ Cheatsheet",
        "type": "cheatsheet",
        "icon": "🚀",
        "domain": "08. Quick Revision & Cheatsheets"
    },
    {
        "id": "08_Real_Forum_Questions_DotNet_SQL_India",
        "filename": "08_Real_Forum_Questions_DotNet_SQL_India.md",
        "title": "08. Real Forum Indian Top 50",
        "badge": "🇮🇳 Indian Hitlist",
        "type": "deep",
        "icon": "🎯",
        "domain": "08. Quick Revision & Cheatsheets"
    },
    {
        "id": "09_DotNet_CLR_Ultra_Deep_Niche_Internals",
        "filename": "09_DotNet_CLR_Ultra_Deep_Niche_Internals.md",
        "title": "09. CLR Ultra-Deep Internals Appendix",
        "badge": "🔬 CLR Internals",
        "type": "deep",
        "icon": "🧠",
        "domain": "09. CLR Ultra-Deep Internals"
    }
]

def build():
    if not os.path.exists(PORTAL_FILE):
        print(f'Error: {PORTAL_FILE} not found!')
        sys.exit(1)

    with open(PORTAL_FILE, 'r', encoding='utf-8') as f:
        html = f.read()

    docs_data = []
    for item in manifest:
        md_path = os.path.join(WORKSPACE_DIR, item['filename'])
        if not os.path.exists(md_path):
            print(f'Warning: {md_path} does not exist!')
            content = ''
        else:
            with open(md_path, 'r', encoding='utf-8') as f_md:
                content = f_md.read()
        doc = dict(item)
        doc['content'] = content
        docs_data.append(doc)

    json_str = json.dumps(docs_data, ensure_ascii=False)
    
    tag_start = '<script id="docsData" type="application/json">'
    tag_end = '</script>'
    
    idx_start = html.find(tag_start)
    if idx_start == -1:
        print('Error: start tag not found')
        sys.exit(1)
    
    idx_end = html.find(tag_end, idx_start)
    if idx_end == -1:
        print('Error: end tag not found')
        sys.exit(1)

    new_html = html[:idx_start + len(tag_start)] + json_str + html[idx_end:]

    with open(PORTAL_FILE, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f'Successfully updated {PORTAL_FILE} with {len(docs_data)} documents ({len(new_html):,} bytes).')

if __name__ == '__main__':
    build()
