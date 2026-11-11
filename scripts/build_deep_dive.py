#!/usr/bin/env python3
"""
Compiler script to assemble 03_Angular_Signals_Deep_Dive.md
"""
import os, sys
from generate_deep_dive import build_deep_dive
from deep_dive_part1 import get_part1_questions
from deep_dive_part2 import get_part2_questions
from deep_dive_part3 import get_part3_questions
from deep_dive_part4 import get_part4_questions, get_architecture_sections

def main():
    header = build_deep_dive()
    
    modules = [
        ("\n# MODULE 1: COMPONENT LIFECYCLE HOOKS & EXECUTION ORDER\n\n", get_part1_questions()[:4]),
        ("\n# MODULE 2: ANGULAR SIGNALS (v16–v18+) REACTIVE PRIMITIVES\n\n", get_part1_questions()[4:8]),
        ("\n# MODULE 3: SIGNALS VS RXJS OBSERVABLES & REACTIVE INTEROP\n\n", get_part1_questions()[8:11]),
        ("\n# MODULE 4: COMPONENT COMMUNICATION ARCHITECTURES\n\n", get_part1_questions()[11:14]),
        ("\n# MODULE 5: RXJS FLATTENING OPERATORS MASTERY\n\n", get_part1_questions()[14:17]),
        ("\n# MODULE 6: CHANGE DETECTION STRATEGIES & ZONELESS ARCHITECTURE\n\n", get_part2_questions()[:3]),
        ("\n# MODULE 7: DIRECTIVES: BUILT-IN CONTROL FLOW & CUSTOM ATTRIBUTES\n\n", get_part2_questions()[3:5]),
        ("\n# MODULE 8: PIPES: PURE VS IMPURE ARCHITECTURE\n\n", get_part2_questions()[5:6]),
        ("\n# MODULE 9: HIERARCHICAL DEPENDENCY INJECTION & PROVIDERS\n\n", get_part2_questions()[6:9]),
        ("\n# MODULE 10: REACTIVE FORMS VS TEMPLATE-DRIVEN FORMS\n\n", get_part2_questions()[9:11]),
        ("\n# MODULE 11: MODERN ROUTING, NAVIGATION & LAZY LOADING\n\n", get_part3_questions()[:3]),
        ("\n# MODULE 12: HTTP CLIENT & FUNCTIONAL INTERCEPTORS\n\n", get_part3_questions()[3:5]),
        ("\n# MODULE 13: MEMORY LEAK PREVENTION & TEARDOWN MECHANICS\n\n", get_part3_questions()[5:7]),
        ("\n# MODULE 14: STATE MANAGEMENT: LOCAL VS NGRX SIGNALSTORE\n\n", get_part3_questions()[7:9]),
        ("\n# MODULE 15: PERFORMANCE TUNING & ENTERPRISE OPTIMIZATIONS\n\n", get_part3_questions()[9:11]),
        ("\n# MODULE 16: BONUS SENIOR INTERVIEW ROUND QUESTIONS\n\n", get_part3_questions()[11:15]),
        ("\n# MODULE 17: PRODUCTION ARCHITECTURE & SYSTEM DESIGN CASE STUDIES\n\n", get_part4_questions())
    ]

    body_parts = []
    for mod_title, qs in modules:
        body_parts.append(mod_title + "\n".join(qs))

    arch_sections = get_architecture_sections()

    full_document = header + "\n\n" + "\n\n".join(body_parts) + "\n\n" + arch_sections

    out_path = '/home/ubermensch/Desktop/interview/03_Angular_Signals_Deep_Dive.md'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_document)

    print(f"Successfully generated {out_path} with 51 questions and 4 architecture sections!")

if __name__ == '__main__':
    main()
