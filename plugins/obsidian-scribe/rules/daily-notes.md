---
paths: "daily-notes/**/*.md"
alwaysApply: false
---

# Daily Notes Rules

These rules apply when working with files in the `daily-notes/` folder.

## File Structure

Daily notes follow this structure:
```
---
type: daily
date: YYYY-MM-DD
tags:
  - "#daily"
---
# Habits
- [ ] [[Walk]] #habit
- [ ] [[Stretch]] #habit
- [ ] [[Vitamins]] #habit
---
# Food
- [food entries here]

---
# Today
## Tasks
[dataviewjs block]
## Log
- [log entries here]
```

## Naming Convention

- Format: `YYYY-MM-DD.md` (ISO date)
- Example: `2025-12-29.md`
- Path: `{config.paths.daily_notes}/YYYY-MM-DD.md`

## Sections

### Habits Section
- Habits tracked as configured in `.obsidian-scribe.json`
- Format: `- [ ] [[Habit]] #habit` (uncompleted) or `- [x] [[Habit]] #habit` (completed)
- Habits are wikilinked to their respective pages

### Food Section
- List food items as bullet points
- One item per line
- Used by food-macros skill for calculation

### Log Section
- Daily activities and accomplishments
- Include timestamps when relevant (HH:MM format)
- Achievements here get extracted to weekly notes
- **CRITICAL: Always APPEND new entries to the bottom of the Log section**
- **Log entries must be in chronological order (oldest first, newest last)**
- **Never prepend or insert entries at the top of the Log section**

#### CRITICAL: Log Entry Formatting Rules

**The Log section MUST be a continuous bullet list - NEVER use `---` or `## Heading` elements!**

**All Log Entries:**
- Just append bullets directly - NO `---` separators, NO `## Headings`
- Format: `- HH:MM Description` or `- HH:MM **Bold** Description`
- Sub-bullets use 2-space indentation
- Use bold text and nested bullets for complex content, NOT markdown structural elements
- Example:
  ```
  - 18:34 **Task completed** - Description here
    - Sub-detail one
    - Sub-detail two
    - More details as needed
  ```

**For Complex Content:**
- Use nested sub-bullets (2-space indents) for details
- Use **bold** text for emphasis or subsection titles
- Keep tables compact or reference external files
- Example:
  ```
  - 17:48 **Major Feature Testing**
    - Comprehensive test of all extension points
    - ✅ All 9 hooks passed
    - ✅ Fixed 5 frontmatter issues
    - Status: Production-ready
  ```

**NEVER DO THIS** (breaks continuous bullet list):
```
- Previous entry

---

## Big Section with Heading

Tables and paragraphs...

- Next entry
```

**ALWAYS DO THIS** (maintains continuous list):
```
- Previous entry
- 17:48 **Big Section Summary**
  - Brief summary of complex work
  - Key accomplishments listed as sub-bullets
  - Link to external documentation if needed
- Next entry
```

**Why:** In Markdown, `---` and `## Heading` elements break list parsing. The entire Log section must remain a continuous bullet list for proper rendering in Obsidian.

## Rules

1. **Use template for new notes** - Read `templates/daily.md` and use it as reference when creating new daily notes
2. **Never modify past entries** - Don't change historical daily notes
3. **Preserve dataviewjs** - Don't alter the Tasks dataviewjs block
4. **Keep separators** - Maintain the `---` section dividers
5. **Habit wikilinks** - Always link habit names as configured
6. **Weight format** - If logging weight, use: `weight is XX.Xkg`
