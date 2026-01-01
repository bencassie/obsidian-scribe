#!/usr/bin/env python3
"""
Wikilink Suggest Hook (wikilink-suggest.py)

Part of the wikilink-* hook family:
- wikilink-cache.py   : SessionStart - Rebuilds entity cache from vault pages
- wikilink-suggest.py : PostToolUse  - Auto-applies wikilinks after edits

Runs after Edit/Write operations to auto-apply wikilinks to known entities.

Detects:
- People names (capitalized multi-word)
- Project names (MyProject, Project 2024, etc.)
- Technologies (Claude Code, Azure, etc.)
- Known entities from wikilink cache

Protected zones (never wikilinked):
- YAML frontmatter
- Code blocks (``` and `)
- Existing wikilinks
- Markdown links
- URLs
- Hashtags (#tag)
- HTML/XML tags (<tag>)
- Obsidian comments (%% ... %%)
- Math expressions ($ ... $)

Exit codes:
- 0: Always (informational only, never blocks)
"""

import json
import sys
import re
from pathlib import Path
from collections import defaultdict

# Configure UTF-8 output for Windows console
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass


# Common words to exclude from wikilink suggestions
EXCLUDE_WORDS = {
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
    'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
    'september', 'october', 'november', 'december',
    'today', 'tomorrow', 'yesterday', 'week', 'month', 'year',
    'the', 'and', 'for', 'with', 'from', 'this', 'that',
    'christmas', 'holiday', 'break',
}


def load_wikilinks_from_cache(vault_path: Path) -> set:
    """Load existing wikilinks from cache file."""
    cache_file = vault_path / '.claude' / 'wikilink-entities.json'

    if not cache_file.exists():
        # Fallback: scan vault if cache doesn't exist
        return extract_existing_wikilinks_fallback(vault_path)

    try:
        cache_data = json.loads(cache_file.read_text(encoding='utf-8'))
        wikilinks = set()

        # Combine all categories (skip metadata)
        for category, entities in cache_data.items():
            if category != '_metadata':
                wikilinks.update(entities)

        return wikilinks
    except Exception:
        # Fallback on error
        return extract_existing_wikilinks_fallback(vault_path)


def extract_existing_wikilinks_fallback(vault_path: Path) -> set:
    """Fallback: Extract all existing wikilinks from the vault."""
    wikilinks = set()

    # Search all markdown files
    for md_file in vault_path.rglob('*.md'):
        # Skip .claude directory
        if '.claude' in str(md_file):
            continue

        try:
            content = md_file.read_text(encoding='utf-8')
            # Match [[wikilink]] and [[wikilink|alias]]
            matches = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
            wikilinks.update(matches)
        except Exception:
            continue

    return wikilinks


def find_frontmatter_end(content: str) -> int:
    """Find where YAML frontmatter ends. Returns 0 if no frontmatter."""
    if not content.startswith('---'):
        return 0

    # Find the closing --- (must be on its own line)
    lines = content.split('\n')
    if len(lines) < 2:
        return 0

    # Start after the opening ---
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == '---':
            # Calculate character position after closing ---
            return sum(len(l) + 1 for l in lines[:i+1])

    return 0  # No closing --- found


def apply_wikilinks(content: str, entities_to_link: list) -> tuple[str, int]:
    """Apply wikilinks to entities in content.

    Returns: (updated_content, count_of_links_added)
    """
    if not entities_to_link:
        return content, 0

    # Sort by length (longest first) to avoid partial replacements
    entities_sorted = sorted(set(entities_to_link), key=len, reverse=True)

    # Skip areas we shouldn't link
    # CRITICAL: Skip YAML frontmatter (first thing in file between --- markers)
    frontmatter_end = find_frontmatter_end(content)
    frontmatter = [(0, frontmatter_end)] if frontmatter_end > 0 else []

    # Remove code blocks
    code_block_pattern = r'```[\s\S]*?```'
    code_blocks = list(re.finditer(code_block_pattern, content))

    # Remove inline code
    inline_code_pattern = r'`[^`]+`'
    inline_codes = list(re.finditer(inline_code_pattern, content))

    # Remove existing wikilinks
    wikilink_pattern = r'\[\[[^\]]+\]\]'
    existing_links = list(re.finditer(wikilink_pattern, content))

    # Remove markdown links [text](url)
    markdown_link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
    markdown_links = list(re.finditer(markdown_link_pattern, content))

    # Remove bare URLs (http:// or https://)
    url_pattern = r'https?://[^\s\)\]]+(?:\([^\)]+\))?[^\s\)\]]*'
    bare_urls = list(re.finditer(url_pattern, content))

    # Remove hashtags (don't wikilink inside tags like #habit, #work)
    hashtag_pattern = r'#[\w-]+'
    hashtags = list(re.finditer(hashtag_pattern, content))

    # Remove HTML/XML tags (angle brackets break Obsidian rendering)
    html_tag_pattern = r'<[^>]+>'
    html_tags = list(re.finditer(html_tag_pattern, content))

    # Remove Obsidian comments (%% ... %%)
    obsidian_comment_pattern = r'%%.*?%%'
    obsidian_comments = list(re.finditer(obsidian_comment_pattern, content, re.DOTALL))

    # Remove math expressions ($ ... $ and $$ ... $$)
    math_block_pattern = r'\$\$[\s\S]*?\$\$|\$[^\$]+\$'
    math_blocks = list(re.finditer(math_block_pattern, content))

    # Combine all skip zones (frontmatter MUST be first to protect it)
    skip_zones = frontmatter + [(m.start(), m.end()) for m in code_blocks + inline_codes + existing_links + markdown_links + bare_urls + hashtags + html_tags + obsidian_comments + math_blocks]
    skip_zones.sort()

    links_added = 0
    new_content = content

    for entity in entities_sorted:
        # Find all occurrences with word boundaries (case-insensitive)
        pattern = r'\b' + re.escape(entity) + r'\b'

        for match in re.finditer(pattern, new_content, re.IGNORECASE):
            start, end = match.start(), match.end()

            # Check if this match is in a skip zone
            in_skip_zone = any(s <= start < e or s < end <= e for s, e in skip_zones)

            if not in_skip_zone:
                # Apply wikilink
                matched_text = match.group()
                wikilinked = f'[[{entity}]]'
                new_content = new_content[:start] + wikilinked + new_content[end:]

                # Update skip zones (shift positions after this insertion)
                shift = len(wikilinked) - len(matched_text)
                skip_zones = [(s if s <= start else s + shift,
                              e if e <= start else e + shift) for s, e in skip_zones]
                # Add this new wikilink to skip zones
                skip_zones.append((start, start + len(wikilinked)))
                skip_zones.sort()

                links_added += 1
                break  # Only link first occurrence to avoid over-linking

    return new_content, links_added


def find_linkable_candidates(content: str, existing_wikilinks: set) -> dict:
    """Find potential wikilink candidates in content."""
    candidates = defaultdict(list)

    # Remove code blocks and already wikilinked content
    # CRITICAL: Remove YAML frontmatter first
    frontmatter_end = find_frontmatter_end(content)
    content_no_code = content[frontmatter_end:] if frontmatter_end > 0 else content
    # Remove fenced code blocks
    content_no_code = re.sub(r'```[\s\S]*?```', '', content_no_code)
    # Remove inline code
    content_no_code = re.sub(r'`[^`]+`', '', content_no_code)
    # Remove existing wikilinks
    content_no_code = re.sub(r'\[\[[^\]]+\]\]', '', content_no_code)
    # Remove markdown links [text](url)
    content_no_code = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', '', content_no_code)
    # Remove bare URLs (http:// or https://)
    content_no_code = re.sub(r'https?://[^\s\)\]]+(?:\([^\)]+\))?[^\s\)\]]*', '', content_no_code)
    # Remove hashtags
    content_no_code = re.sub(r'#[\w-]+', '', content_no_code)
    # Remove HTML/XML tags
    content_no_code = re.sub(r'<[^>]+>', '', content_no_code)
    # Remove Obsidian comments
    content_no_code = re.sub(r'%%.*?%%', '', content_no_code, flags=re.DOTALL)
    # Remove math expressions
    content_no_code = re.sub(r'\$\$[\s\S]*?\$\$|\$[^\$]+\$', '', content_no_code)

    # Pattern 1: Capitalized multi-word phrases (2-4 words)
    multi_word_pattern = r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\b'
    for match in re.finditer(multi_word_pattern, content_no_code):
        phrase = match.group(1)
        if phrase.lower() not in EXCLUDE_WORDS:
            # Check if phrase exists in vault
            if phrase in existing_wikilinks:
                candidates['Multi-Word Entities'].append(phrase)

    # Pattern 2: Known acronyms (2-6 uppercase letters)
    acronym_pattern = r'\b([A-Z]{2,6})\b'
    for match in re.finditer(acronym_pattern, content_no_code):
        acronym = match.group(1)
        if acronym in existing_wikilinks:
            candidates['Acronyms/Projects'].append(acronym)

    # Pattern 3: Technology/tool names (known from existing wikilinks)
    for wikilink in existing_wikilinks:
        # Use word boundaries to avoid partial matches
        pattern = r'\b' + re.escape(wikilink) + r'\b'
        if re.search(pattern, content_no_code, re.IGNORECASE):
            if any(char.isupper() for char in wikilink) and any(char.islower() for char in wikilink):
                candidates['Existing Entities'].append(wikilink)

    # Deduplicate each category
    for category in candidates:
        candidates[category] = sorted(set(candidates[category]))

    return candidates


def main():
    try:
        # Read hook input from stdin
        hook_input = json.load(sys.stdin)

        # CRITICAL: Only run auto-fixes on Edit/Write, not Read
        tool_name = hook_input.get('tool_name', '')
        if tool_name not in ['Edit', 'Write']:
            sys.exit(0)

        # Get the file path from tool input
        tool_input = hook_input.get('tool_input', {})
        file_path = tool_input.get('file_path', '')

        # Only check markdown files
        if not file_path.endswith('.md'):
            sys.exit(0)

        # Skip .claude directory
        if '.claude' in file_path:
            sys.exit(0)

        # Check if file exists
        path = Path(file_path)
        if not path.exists():
            sys.exit(0)

        # Get vault root (assuming file is in vault)
        vault_path = path
        while vault_path.parent != vault_path:
            if (vault_path / '.obsidian').exists() or (vault_path / '.claude').exists():
                break
            vault_path = vault_path.parent

        # Load existing wikilinks from cache
        existing_wikilinks = load_wikilinks_from_cache(vault_path)

        # Read file content
        content = path.read_text(encoding='utf-8')

        # Find linkable candidates
        candidates = find_linkable_candidates(content, existing_wikilinks)

        # Remove empty categories
        candidates = {k: v for k, v in candidates.items() if v}

        if candidates:
            # Collect all entities to link
            all_entities = []
            for items in candidates.values():
                all_entities.extend(items)

            # Apply wikilinks automatically
            updated_content, links_added = apply_wikilinks(content, all_entities)

            if links_added > 0:
                # Write updated content back to file
                path.write_text(updated_content, encoding='utf-8')

                print(f"\n✓ Auto-Applied {links_added} Wikilinks to {path.name}")
                print("-" * 60)

                for category, items in candidates.items():
                    # Show what was linked (limit to top 5 per category)
                    display_items = items[:min(5, len(items))]
                    print(f"{category}: {', '.join(display_items)}")
                    if len(items) > 5:
                        print(f"  ... and {len(items) - 5} more")

                print("-" * 60)
                print("")

        sys.exit(0)

    except json.JSONDecodeError:
        sys.exit(0)
    except FileNotFoundError as e:
        print(f"[obsidian-scribe] Wikilink suggest: File not found - {e.filename}", file=sys.stderr)
        sys.exit(0)
    except PermissionError as e:
        print(f"[obsidian-scribe] Wikilink suggest: Permission denied - {e.filename}", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"[obsidian-scribe] Wikilink suggest error: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(0)


if __name__ == '__main__':
    main()
