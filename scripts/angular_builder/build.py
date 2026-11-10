import os
import sys

# Import builder parts
from part0_header import HEADER
from part1_lifecycle import MODULE_1
from part2_signals import MODULE_2
from part3_signals_rxjs import MODULE_3
from part4_communication import MODULE_4
from part5_flattening import MODULE_5
from part6_change_detection import MODULE_6
from part7_directives import MODULE_7
from part8_pipes import MODULE_8
from part9_di import MODULE_9
from part10_forms import MODULE_10
from part11_routing import MODULE_11
from part12_http import MODULE_12
from part13_memory import MODULE_13
from part14_state import MODULE_14
from part15_perf import MODULE_15
from part16_bonus import MODULE_16
from part17_advanced_ref import ADVANCED_REF_HEADER

def extract_original_case_studies(original_file_path):
    with open(original_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    def get_slice(start, end):
        return ''.join(lines[start-1:end])

    # Slices based on exact line indexes identified
    cs1_body = get_slice(44, 170)
    cs2_body = get_slice(434, 619)
    cs3_body = get_slice(725, 860)
    cs4_body = get_slice(1028, 1193)
    cs5_body = get_slice(1319, 1468)
    cs6_body = get_slice(1488, 1632)
    cs7_body = get_slice(1741, 1890)
    cs8_body = get_slice(4355, 4513)

    case_studies = [
        ("## 💼 Case Study 1: Enterprise Banking Dashboard Migration (NgModule to Modern Standalone + Control Flow)", cs1_body),
        ("## 💼 Case Study 2: High-Throughput E-Commerce Cart & Live Pricing (Push-Pull Signal Graph)", cs2_body),
        ("## 💼 Case Study 3: High-Scale Typeahead Catalog Search with Race-Condition Prevention", cs3_body),
        ("## 💼 Case Study 4: High-Frequency Institutional FX Trading Modal (Detached DOM Leak Prevention)", cs4_body),
        ("## 💼 Case Study 5: High-Frequency 60 FPS Order Book Depth Heatmap (NgZone Escaping & OnPush)", cs5_body),
        ("## 💼 Case Study 6: Corporate Banking Portal Silent JWT Refresh & Atomic Route Guard", cs6_body),
        ("## 💼 Case Study 7: Full NgRx SignalStore Production Implementation with Custom Features (withStorageSync, withLogger)", cs7_body),
        ("## 💼 Case Study 8: Real-Time Polling Dashboard Widget with Senior Cleanup Architecture", cs8_body)
    ]
    
    formatted_case_studies = []
    for heading, body in case_studies:
        # Strip leading ### title from original body so we don't have duplicate heading
        body_lines = body.strip().splitlines()
        if body_lines and body_lines[0].startswith('### 💼 Concrete Real-World Production Example'):
            cleaned_body = '\n'.join(body_lines[1:]).strip()
        else:
            cleaned_body = body.strip()
        formatted_case_studies.append(f"{heading}\n\n{cleaned_body}\n\n---\n")

    return '\n'.join(formatted_case_studies)

def main():
    workspace_dir = '/home/ubermensch/Desktop/interview'
    original_file = os.path.join(workspace_dir, '03_Angular_Signals_Deep_Dive.md')
    output_file = os.path.join(workspace_dir, '03_Angular_Signals_Deep_Dive.md')

    print("Extracting original case studies and deep code...")
    case_studies_content = extract_original_case_studies(original_file)

    print("Assembling master guide...")
    document_parts = [
        HEADER.strip(),
        MODULE_1.strip(),
        MODULE_2.strip(),
        MODULE_3.strip(),
        MODULE_4.strip(),
        MODULE_5.strip(),
        MODULE_6.strip(),
        MODULE_7.strip(),
        MODULE_8.strip(),
        MODULE_9.strip(),
        MODULE_10.strip(),
        MODULE_11.strip(),
        MODULE_12.strip(),
        MODULE_13.strip(),
        MODULE_14.strip(),
        MODULE_15.strip(),
        MODULE_16.strip(),
        ADVANCED_REF_HEADER.strip(),
        case_studies_content.strip()
    ]

    full_document = '\n\n'.join(document_parts) + '\n'

    # Backup original file first just in case
    backup_file = os.path.join(workspace_dir, '03_Angular_Signals_Deep_Dive.md.bak')
    if not os.path.exists(backup_file):
        with open(original_file, 'r', encoding='utf-8') as src, open(backup_file, 'w', encoding='utf-8') as dst:
            dst.write(src.read())
        print(f"Backup created at: {backup_file}")

    print(f"Writing assembled master guide to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_document)

    print(f"Done! Written {len(full_document)} characters to {output_file}.")

if __name__ == '__main__':
    main()
