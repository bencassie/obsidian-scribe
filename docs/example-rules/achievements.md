---
# This is an EXAMPLE rule file for documentation purposes
# Copy this to your vault's .claude/rules/ directory and adapt the paths to match your vault structure

# Claude Code scoping (example - adapt to your vault)
paths: "path/to/your/Achievements.md"
alwaysApply: false

# Obsidian metadata (optional - for vault organization)
type: rule
tags:
  - rule
  - achievements
  - automation
  - format
aliases:
  - Achievement Format Rules
date: 2026-01-01
description: Format requirements for the Achievements.md log file
---

# Achievement Log Format Rules (Example)

> **Note**: This is an example rule file showing how to configure achievement tracking in your vault.
> The achievement-detect hook and achievement-extraction-agent use this format when writing to your Achievements file.

These rules apply when writing to or modifying the Achievements.md file.

## File Location

- Path: Configurable (e.g., `personal/goals/Achievements.md` or `Achievements.md`)
- Type: Chronological achievement log
- Auto-updated by: achievement-detect hook, achievement-extraction-agent (part of obsidian-scribe)

## Format Requirements

### Entry Format

Every achievement entry MUST follow this exact format:

```markdown
- YYYY-MM-DD HH:MM - Achievement text here
```

**Examples:**
```markdown
- 2025-12-31 14:30 - Successfully deployed Paris Alignment API to production
- 2026-01-01 09:15 - Completed comprehensive vault health audit
```

### Structure

```markdown
---
type: achievement
tags:
  - achievement
  - career
aliases:
  - Work Achievements
---

# Work Achievements

## YYYY

### Month YYYY
- YYYY-MM-DD HH:MM - Achievement text
- YYYY-MM-DD HH:MM - Achievement text

### Month YYYY
- YYYY-MM-DD HH:MM - Achievement text
```

## Critical Rules

### Timestamps

- **ALWAYS include timestamps** in format: `YYYY-MM-DD HH:MM`
- Timestamps use 24-hour format (e.g., 14:30, not 2:30 PM)
- Timestamp represents when the achievement was recorded, not when it occurred
- Format separator: space-dash-space between timestamp and achievement text

### Chronological Order

- Entries within each month MUST be in chronological order (oldest first)
- New achievements are APPENDED to the end of the month section
- Never insert achievements in the middle of existing entries
- This maintains append-only log structure

### Monthly Sections

- Organized by month: `### December 2025`
- Month format: Full month name + space + 4-digit year
- Months appear within year sections: `## 2025`
- New month sections are created automatically as needed

### Deduplication

- **No duplicate achievements** allowed in the file
- Automated deduplication uses normalized comparison:
  - Ignores timestamps, bullets, formatting
  - Case-insensitive
  - Compares first 60 characters
  - Removes wikilink brackets for comparison
- If similar achievement exists, new one is skipped

### Automated Writing

When hooks/agents write achievements:
- Use `write_achievements_to_file()` from achievement_detector library
- Timestamps are automatically added by the library
- Deduplication is handled automatically
- Maximum 3 achievements per hook invocation (prevents spam)
- Maximum 10 achievements per agent batch operation

### Manual Edits

When manually editing Achievements.md:
- Preserve timestamp format exactly
- Maintain chronological order within months
- Use estimated timestamps for backdated entries
- Follow existing wikilink patterns in the file

## Examples

### Good Format

```markdown
### January 2026
- 2026-01-01 09:00 - Completed vault health audit with 941 orphans identified
- 2026-01-01 14:30 - Cleaned up Achievements.md: removed 20+ duplicates
- 2026-01-01 15:45 - Updated achievement-detect hook with timestamp support
```

### Bad Format

```markdown
### January 2026
- Completed vault health audit  ❌ (missing timestamp)
- 01/01/2026 - Fixed duplicates  ❌ (wrong date format)
- 2026-01-01 2:30pm - Updated hook  ❌ (12-hour format)
- 2026-01-01 09:00 Updated hook  ❌ (missing dash separator)
```

## Automation Details

### achievement-detect Hook

- Runs after Edit/Write operations on daily notes
- Detects achievements using liberal keyword matching
- Auto-adds up to 3 achievements per run
- Adds timestamp at detection time
- Output format: `- YYYY-MM-DD HH:MM - [achievement text]`

### achievement-extraction-agent

- Batch processes multiple notes (weekly/monthly rollups)
- Scans for achievements using same detection library
- Auto-adds up to 10 achievements per batch
- All achievements get same timestamp (batch processing time)
- Used for retroactive achievement extraction

### Deduplication Strategy

Normalization process for comparison:
1. Remove timestamps: `- 2025-12-31 14:30 ` → ``
2. Remove bullets: `- ` → `___INLINE_CODE_19[[API]]INLINE_CODE_20___API`
4. Remove bold/italic: `**text**` → `text`
5. Normalize whitespace
6. Take first 60 characters
7. Convert to lowercase

Example:
- Original: `- 2025-12-31 14:30 - Successfully deployed [[Paris Alignment]] API`
- Normalized: `successfully deployed paris alignment api`
- Comparison: First 60 chars, case-insensitive

## Week Number Reference

While not stored in the file, achievements can be queried by week:

___CODE_BLOCK_5___

## Search Patterns

The timestamp format enables powerful searches:

___CODE_BLOCK_6___

## Integration with Other Systems

### Daily Notes

- Achievements are detected from daily note log sections
- Format in daily notes can be freeform
- Detection uses liberal keyword matching
- Original formatting is preserved in daily notes

### Weekly Notes

- Weekly rollup can trigger achievement extraction
- Achievements are sourced from daily notes in that week
- All achievements from the week get current timestamp when extracted

### Monthly Notes

- Monthly rollup can trigger achievement extraction
- Achievements are sourced from all daily notes in that month
- Useful for capturing achievements that weren't auto-detected

## Configuration

To use this rule in your vault:

1. **Copy to your vault**: `.claude/rules/achievements.md`
2. **Update the `paths` field** in frontmatter to point to your Achievements file
3. **Configure achievement file path** in `.obsidian-scribe.json`:
   ___CODE_BLOCK_7___
4. **Customize log section** in config if needed (default is `## Log`)

## Maintenance

### Regular Review

Monthly review checklist:
- Verify chronological order within each month
- Check for any duplicate entries that slipped through
- Ensure all entries have proper timestamp format
- Validate month section headers are correct

### Cleanup

If issues are found:
1. Back up Achievements.md first
2. Read entire file to understand current state
3. Use Edit tool with exact text matching for corrections
4. Maintain chronological order when fixing
5. Preserve all wikilinks and formatting

### Testing Achievement Detection

Test achievement detection on a daily note:

```bash
python -c "
import sys
from pathlib import Path

# Adjust path to your obsidian-scribe installation
plugin_root = Path('path/to/obsidian-scribe/plugins/obsidian-scribe')
sys.path.insert(0, str(plugin_root / 'hooks'))
sys.path.insert(0, str(plugin_root))

from config.loader import load_config
from hooks.lib.achievement_detector import check_for_achievements

config = load_config()
content = open('daily-notes/2026-01-01.md').read()
achievements = check_for_achievements(content, config)
print(f'Found {len(achievements)} achievements')
for a in achievements[:5]:
    print(f'  - {a[\"line\"][:80]}')
"
```

## Related Documentation

- [Achievement Detection Library](../../plugins/obsidian-scribe/hooks/lib/achievement_detector.py)
- [Achievement-Detect Hook](../../plugins/obsidian-scribe/hooks/achievement-detect.py)
- [Achievement-Extraction Agent](../../plugins/obsidian-scribe/agents/achievement/achievement-extraction-agent.md)
- [Configuration Schema](../../plugins/obsidian-scribe/config/schema.json)
