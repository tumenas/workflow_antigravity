#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Cochrane Writing Style Linter
Audits academic paper drafts (.qmd or .tex) against John Cochrane's writing guidelines.
"""

import sys
import re
import os

# Regex rules for Cochrane's style guide
PASSIVE_VOICE = re.compile(
    r'\b(is|are|was|were|been)\s+(assumed|constructed|computed|estimated|analyzed|determined|found|used|run|done|tested|presented|derived|specified|plotted|shown|reported|calculated)\b',
    re.IGNORECASE
)

NAKED_THIS = re.compile(
    r'\b(this|This)\s+(shows|implies|suggests|indicates|proves|means|is|was|were|leads|helps|can|will|has)\b'
)

MODEL_WHERE = re.compile(
    r'\b(model|equation|specification|regression|framework|setting)\s+where\b',
    re.IGNORECASE
)

EXCESS_PRECISION = re.compile(
    r'\b\d+\.\d{4,}\b'
)

# Custom rule lists
FORBIDDEN_PHRASES = [
    (re.compile(r'it should be noted that', re.IGNORECASE), 
     "Cochrane: 'It should be noted that' is particularly obnoxious. Just say what you want to say directly."),
    (re.compile(r'it is easy to show that', re.IGNORECASE), 
     "Cochrane: 'It is easy to show that' usually means it isn't. Just show it or omit the phrase."),
    (re.compile(r'a comment is in order', re.IGNORECASE), 
     "Cochrane: Strike 'A comment is in order at this point.' Just make the comment."),
    (re.compile(r'leave\s+\w+\s+for future research', re.IGNORECASE), 
     "Cochrane: Strike 'I leave x for future research.' We are less interested in your plans and excuses than in your memoirs."),
    (re.compile(r'illustrative (test|empirical|work)', re.IGNORECASE), 
     "Cochrane: Never do 'illustrative' work. Do real empirical work or don't do any at all."),
    (re.compile(r'\butilize\b', re.IGNORECASE), 
     "Cochrane: Use simple short words. Use 'use' instead of 'utilize'."),
    (re.compile(r'\butilizing\b', re.IGNORECASE), 
     "Cochrane: Use 'using' instead of 'utilizing'."),
    (re.compile(r'\bstriking\b', re.IGNORECASE), 
     "Cochrane: Avoid adjectives to describe your own work (e.g. 'striking'). Let the reader judge."),
    (re.compile(r'\bvery significant\b', re.IGNORECASE), 
     "Cochrane: Avoid adjectives like 'very significant'. Specify if it is statistically or economically significant, and give magnitudes."),
    (re.compile(r'\bvery novel\b', re.IGNORECASE), 
     "Cochrane: Avoid self-praise like 'very novel'."),
    (re.compile(r'\bFF\b'), 
     "Cochrane: Don't abbreviate authors' names (e.g. Fama and French, not FF). There is always enough space to spell out people's names."),
]


def audit_file(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        sys.exit(1)

    print("=" * 80)
    print(f"COCHRANE STYLE AUDIT: {os.path.basename(filepath)}")
    print("=" * 80)

    violations_count = 0
    in_code_block = False

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for idx, line in enumerate(f, 1):
            stripped = line.strip()

            # Ignore markdown code blocks
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue

            if in_code_block:
                continue

            # Ignore comments in markdown or latex
            if stripped.startswith("%") or stripped.startswith("<!--"):
                continue

            # 1. Passive Voice Check
            passive_matches = PASSIVE_VOICE.findall(line)
            if passive_matches:
                for match in passive_matches:
                    phrase = f"{match[0]} {match[1]}"
                    print(f"Line {idx:4d} | [PASSIVE VOICE] | Found: '{phrase}'")
                    print(f"          -> Cochrane: Use active voice. Search for 'is' and 'are' to root out passive sentences.")
                    print(f"          -> Context: {stripped[:100]}")
                    print("-" * 80)
                    violations_count += 1

            # 2. Naked This Check
            naked_matches = NAKED_THIS.findall(line)
            if naked_matches:
                for match in naked_matches:
                    phrase = f"{match[0]} {match[1]}"
                    print(f"Line {idx:4d} | [NAKED 'THIS']   | Found: '{phrase}'")
                    print(f"          -> Cochrane: Clothe the naked 'this'. Follow it with a noun (e.g. 'this regression shows...').")
                    print(f"          -> Context: {stripped[:100]}")
                    print("-" * 80)
                    violations_count += 1

            # 3. Model Where Check
            where_matches = MODEL_WHERE.findall(line)
            if where_matches:
                for match in where_matches:
                    phrase = f"{match[0]} where"
                    print(f"Line {idx:4d} | ['WHERE' IN MODEL]| Found: '{phrase}'")
                    print(f"          -> Cochrane: 'Where' refers to a place. Use 'in which' for models (e.g. 'models in which...').")
                    print(f"          -> Context: {stripped[:100]}")
                    print("-" * 80)
                    violations_count += 1

            # 4. Excess Precision Check
            precision_matches = EXCESS_PRECISION.findall(line)
            if precision_matches:
                for num in precision_matches:
                    print(f"Line {idx:4d} | [EXCESS DECIMALS] | Found: '{num}'")
                    print(f"          -> Cochrane: Use correct significant digits. 2 to 3 digits are plenty for economics (e.g. 4.6 (0.7)).")
                    print(f"          -> Context: {stripped[:100]}")
                    print("-" * 80)
                    violations_count += 1

            # 5. Forbidden Phrases Checks
            for regex, suggestion in FORBIDDEN_PHRASES:
                phrase_matches = regex.findall(line)
                if phrase_matches:
                    for match in phrase_matches:
                        # Match could be a tuple or string depending on regex capture groups
                        matched_str = match if isinstance(match, str) else " ".join(match)
                        print(f"Line {idx:4d} | [BAD PHRASE]     | Found phrase matching pattern")
                        print(f"          -> {suggestion}")
                        print(f"          -> Context: {stripped[:100]}")
                        print("-" * 80)
                        violations_count += 1

    print("=" * 80)
    print(f"Audit completed. Found {violations_count} potential Cochrane style violations.")
    print("=" * 80)
    return violations_count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python audit_cochrane.py <path_to_draft_file>")
        sys.exit(1)

    audit_file(sys.argv[1])
