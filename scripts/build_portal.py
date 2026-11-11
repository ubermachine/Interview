#!/usr/bin/env python3
import os, json, sys

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_FILE = os.path.join(WORKSPACE_DIR, 'scripts', 'portal_template.html')
PORTAL_FILE = os.path.join(WORKSPACE_DIR, 'Study_Portal.html')
INDEX_FILE = os.path.join(WORKSPACE_DIR, 'index.html')

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
        "id": "02_SQL_Server_Performance_Tuning",
        "filename": "02_SQL_Server_Performance_Tuning.md",
        "title": "02. SQL Server Performance Tuning",
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
        "id": "03_Angular_Signals_RxJS",
        "filename": "03_Angular_Signals_RxJS.md",
        "title": "03. Angular Signals + RxJS",
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
        "id": "04_Microservices_SystemDesign",
        "filename": "04_Microservices_SystemDesign.md",
        "title": "04. Microservices System Design",
        "badge": "🟣 Deep Dive",
        "type": "deep",
        "icon": "🧩",
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
    if not os.path.exists(TEMPLATE_FILE):
        print(f'Error: Template {TEMPLATE_FILE} not found!')
        sys.exit(1)

    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template = f.read()

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

    json_raw = json.dumps(docs_data, ensure_ascii=False)
    # Strictly escape '<' and '>' so that no HTML tag (especially </script>) can trigger the HTML parser
    json_safe = json_raw.replace('<', r'\u003c').replace('>', r'\u003e')

    placeholder = '<!-- DOCS_DATA_PLACEHOLDER -->'
    if placeholder not in template:
        print(f'Error: {placeholder} not found in template!')
        sys.exit(1)

    rendered_html = template.replace(placeholder, json_safe)

    with open(PORTAL_FILE, 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    print(f'Successfully generated {PORTAL_FILE} and {INDEX_FILE} ({len(rendered_html):,} bytes, {len(docs_data)} documents).')

if __name__ == '__main__':
    build()
