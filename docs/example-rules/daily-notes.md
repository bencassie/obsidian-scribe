---
# This is an EXAMPLE rule file for documentation purposes
# Copy this to your vault's .claude/rules/ directory and adapt to your vault structure

# Claude Code scoping (example - adapt to your daily notes folder)
paths: "daily-notes/**/*.md"
alwaysApply: false

# Obsidian metadata (optional - for vault organization)
type: rule
tags:
  - rule
  - daily-notes
  - periodic-notes
  - format
aliases:
  - Daily Notes Rules
date: 2026-01-01
description: Format requirements for daily notes used by obsidian-scribe rollup chain
---

# Daily Notes Rules (Example)

> **Note**: This is an example rule file showing recommended daily note structure for obsidian-scribe.
> The rollup chain (weekly/monthly/quarterly/yearly agents) reads from daily notes, so consistent formatting helps.

These rules apply when working with files in your daily notes folder.

## File Structure

Daily notes can follow this structure (adapt to your needs):

```markdown
---
type: daily
date: YYYY-MM-DD
tags:
  - daily
---

# Habits
- [ ] Morning routine #habit
- [ ] Exercise #habit
- [ ] Journal #habit

---

# Log
- HH:MM Log entry 1
- HH:MM Log entry 2
  - Sub-detail with 2-space indent
  - Additional context
- HH:MM Log entry 3
```

**Key Sections for obsidian-scribe:**
- **Log** section: Achievement detection and rollup source
- **Frontmatter**: Date field used by rollup chain for grouping

## Naming Convention

- Format: `YYYY-MM-DD.md` (ISO date format)
- Example: `2025-12-29.md`
- Path: Configurable in `.obsidian-scribe.json` (default: `daily-notes/`)

**Why ISO dates?**
- Sorts chronologically in file explorers
- Easy to parse programmatically
- Works across all platforms
- Standard format used by rollup chain

## Log Section - Critical Formatting Rules

The Log section is where obsidian-scribe detects achievements and extracts content for rollups.

### CRITICAL: Maintain Continuous Bullet List

**The Log section MUST be a continuous bullet list - NEVER use `---` or `## Heading` elements inside it!**

**All Log Entries:**
- Just append bullets directly - NO `---` separators, NO `## Headings` within the Log section
- Format: `- HH:MM Description` or `- HH:MM **Bold** Description`
- Sub-bullets use 2-space indentation
- Use bold text and nested bullets for complex content, NOT markdown structural elements

**Good Example:**
```markdown
## Log
- 09:00 Started work on feature X
- 12:30 **Lunch break** - Met with team
  - Discussed roadmap
  - Reviewed priorities
- 14:00 Completed feature X implementation
  - Fixed 3 bugs
  - Added tests
  - Updated docs
- 18:00 Deployed to staging
```

**Bad Example** (breaks list parsing):
```markdown
## Log
- 09:00 Started work

---

## Afternoon Work

Did some stuff

- 18:00 Finished
```

**Why this matters:**
- In Markdown, `---` and `## Heading` break list parsing
- obsidian-scribe's achievement detector scans the Log section as a continuous list
- Obsidian renders broken lists incorrectly
- The entire Log section must remain a continuous bullet list

### Chronological Order

**ALWAYS append new entries to the bottom of the Log section:**
- Oldest entries at top
- Newest entries at bottom
- Never prepend or insert in the middle

**Why?**
- Maintains narrative flow
- Makes it easy to find recent work (scroll to bottom)
- Rollup agents process in chronological order
- Achievement detection works better with time-ordered entries

### Timestamps

Include timestamps (HH:MM format) for log entries:
- Helps track when work was done
- Enables time-based queries
- Used by achievement detector to identify late-night work

**Format:** `- HH:MM Description`

**Example:**
```markdown
- 09:15 Reviewed pull requests
- 14:30 Deployed to production
- 22:45 Fixed critical bug (late night work - achievement!)
```

### Complex Content Formatting

For detailed content, use nested bullets and bold text:

```markdown
- 17:48 **Major Feature Testing**
  - Comprehensive test of all extension points
  - ✅ All 9 hooks passed
  - ✅ Fixed 5 issues
  - Status: Production-ready
```

**NOT** structural markdown elements:
```markdown
❌ Don't do this:
- 17:48 Work started

## Testing Results

| Test | Result |
|------|--------|
| ... | ... |

- 18:00 Done
```

## Achievement Detection

The achievement-detect hook scans the Log section for significant accomplishments.

### What Gets Detected

Keywords that trigger achievement detection:
- Action verbs: built, deployed, completed, fixed, resolved, implemented
- Success indicators: ✅, passed, working, successful
- First-time events: first time, finally, breakthrough
- Late night work: timestamps between 22:00-05:00

### Examples

**Detected as achievements:**
```markdown
- 14:30 Successfully deployed Paris Alignment API to production
- 15:45 Fixed critical bug affecting 1000+ users
- 22:15 Finally got the database migration working
- 09:00 Built complete ADO pipeline dashboard
```

**Not detected:**
```markdown
- 10:00 Meeting with team
- 12:00 Lunch
- 14:00 Reading documentation
```

## Integration with Rollup Chain

Daily notes are the source for the rollup chain:

```
Daily Notes → Weekly Summaries → Monthly Summaries → Quarterly → Yearly
```

### How It Works

1. **Weekly rollup**: Scans all daily notes in a week
   - Extracts Log section entries
   - Groups achievements
   - Creates weekly summary

2. **Monthly rollup**: Summarizes weekly notes
   - Higher-level summary
   - Key themes and patterns

3. **Quarterly/Yearly**: Further summarization
   - Strategic view
   - Major accomplishments

### What Gets Extracted

From daily notes, rollup agents extract:
- **Achievements** (detected via keywords)
- **Log entries** (for context and narrative)
- **Habits/metrics** (if configured)
- **Tasks completed** (if using task tracking)

## Configuration

To use this rule in your vault:

1. **Copy to your vault**: `.claude/rules/daily-notes.md`
2. **Update the `paths` field** to match your daily notes folder
3. **Configure daily notes path** in `.obsidian-scribe.json`:
   ```json
   {
     "paths": {
       "daily_notes": "daily-notes"
     },
     "sections": {
       "log": "## Log"
     }
   }
   ```

## Best Practices

### Do's ✅
- Use ISO date format for filenames (YYYY-MM-DD.md)
- Keep Log section as continuous bullet list
- Append new entries to bottom (chronological order)
- Include timestamps (HH:MM) for time tracking
- Use nested bullets for complex content
- Be specific and descriptive in log entries

### Don'ts ❌
- Don't use `---` or `## Headings` inside Log section
- Don't prepend entries (breaks chronological order)
- Don't modify past daily notes (preserve history)
- Don't use generic/vague descriptions
- Don't skip timestamps for significant work

## Template

Example daily note template:

```markdown
---
type: daily
date: {{date:YYYY-MM-DD}}
tags:
  - daily
---

# {{date:YYYY-MM-DD}}

## Log
- {{time:HH:mm}}
```

Save this as `templates/daily.md` and use Obsidian's template plugin or manually.

## Related Documentation

- [Rollup Chain Overview](../workflows.md)
- [Achievement Detection](../features/achievements.md)
- [Weekly Rollup Agent](../../plugins/obsidian-scribe/agents/rollup/weekly-agent.md)
- [Configuration Schema](../../plugins/obsidian-scribe/config/schema.json)
