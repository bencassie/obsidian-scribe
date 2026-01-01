#!/usr/bin/env python3
"""
Test the heuristic wikilink detection system.
Standalone script to verify patterns are working correctly.
"""

import re
from collections import defaultdict

# Sample text with various patterns
TEST_TEXT = """
# Test Content

I'm working with Claude Code to build a Machine Learning pipeline.
The Neural Network uses Transformer Models for Natural Language Processing.

The API Server connects to the Graph Database using Entity Framework.
We're building a React App with Node Server backend.

I upgraded to Quest 3 and Python 3 for the project. We're using .NET 8
with GPT-4 integration. The SIP 2024 initiative uses React v18.2.

The PowerBI dashboard connects to GraphAPI and pulls data from TruCost and ESGHub.

The API Management platform handles REST API calls. The MCP Server provides
HTTP POST endpoints. Our SQL Database stores the data.

I went for a walk this morning. It's a good morning. Thank you for reading.
"""

EXCLUDE_WORDS = {
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
    'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
    'september', 'october', 'november', 'december',
    'today', 'tomorrow', 'yesterday', 'week', 'month', 'year',
    'the', 'and', 'for', 'with', 'from', 'this', 'that',
    'christmas', 'holiday', 'break',
}

EXCLUDE_PHRASES = {
    'go for', 'next step', 'good morning', 'happy birthday',
    'thank you', 'please see', 'best regards', 'kind regards',
}

def find_heuristic_candidates(content: str) -> dict:
    """Find high-probability wikilink candidates."""
    heuristic = defaultdict(list)

    # Category 1: Capitalized Multi-Word Phrases (2-4 words)
    multi_word_pattern = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\b'
    for match in re.finditer(multi_word_pattern, content):
        phrase = match.group(1)
        phrase_lower = phrase.lower()

        if phrase_lower in EXCLUDE_WORDS or phrase_lower in EXCLUDE_PHRASES:
            continue

        words = phrase.split()
        if any(w.lower() in EXCLUDE_WORDS for w in words):
            continue

        heuristic['Multi-Word Proper Nouns'].append(phrase)

    # Category 2: Technology Patterns
    tech_suffixes = ['Server', 'API', 'Framework', 'Code', 'Database', 'Platform',
                     'Service', 'Engine', 'Client', 'Library', 'Tool', 'App']
    tech_pattern = r'\b([A-Z][a-z]+(?:\s+(?:' + '|'.join(tech_suffixes) + r')))\b'
    for match in re.finditer(tech_pattern, content):
        phrase = match.group(1)
        heuristic['Technology Terms'].append(phrase)

    dotjs_pattern = r'\b([A-Z][a-z]+\.(?:js|py|net|go|rb|rs))\b'
    for match in re.finditer(dotjs_pattern, content, re.IGNORECASE):
        phrase = match.group(1)
        heuristic['Technology Terms'].append(phrase)

    # Category 3: Version/Year Patterns
    version_patterns = [
        r'\b([A-Z][a-z]+\s+\d{1,2})\b',
        r'\b(\.NET\s+\d)\b',
        r'\b([A-Z]{2,}\s+\d{4})\b',
        r'\b(GPT-\d+(?:\.\d+)?)\b',
        r'\b([A-Z][a-z]+\s+v?\d+(?:\.\d+)*)\b',
    ]
    for pattern in version_patterns:
        for match in re.finditer(pattern, content):
            phrase = match.group(1)
            heuristic['Versioned Products'].append(phrase)

    # Category 4: CamelCase/PascalCase
    camelcase_pattern = r'\b([A-Z][a-z]+[A-Z][a-z][A-Za-z]*)\b'
    for match in re.finditer(camelcase_pattern, content):
        phrase = match.group(1)
        if len(phrase) >= 5:
            heuristic['CamelCase Terms'].append(phrase)

    # Category 6: Acronym + Word/Acronym
    acronym_word_patterns = [
        r'\b([A-Z]{2,6}\s+[A-Z][a-z]+)\b',
        r'\b([A-Z]{2,6}\s+[A-Z]{2,6})\b',
    ]
    for pattern in acronym_word_patterns:
        for match in re.finditer(pattern, content):
            phrase = match.group(1)
            heuristic['Acronym Compounds'].append(phrase)

    # Deduplicate
    for category in heuristic:
        heuristic[category] = sorted(set(heuristic[category]))

    return heuristic


def main():
    print("=" * 70)
    print("HEURISTIC WIKILINK DETECTION TEST")
    print("=" * 70)
    print()

    results = find_heuristic_candidates(TEST_TEXT)

    if not results:
        print("❌ No heuristic patterns detected!")
        return

    total = sum(len(v) for v in results.values())
    print(f"✓ Found {total} heuristic wikilink candidates\n")

    for category, items in results.items():
        print(f"\n{category}:")
        print("-" * 60)
        for item in items:
            print(f"  • {item}")

    print("\n" + "=" * 70)


if __name__ == '__main__':
    main()
