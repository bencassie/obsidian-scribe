# Daily Logging 🦉📝

*Hoot! Let the owl help You capture your daily wisdom with ease.*

Daily logging Features help you record your work, tasks, and thoughts without leaving Claude Code.

## Features in This Domain

| Feature | Type | Purpose |
|---------|------|---------|
| `/auto-log` | Skill | Add timestamped entries to Daily Notes |
| `/task-add` | Skill | Create tasks with due dates |
| `session-start` | Hook | Show Vault Status at Session start |

**No MCP Required** - These features work out of the box!

## `/auto-log` - Timestamped Logging

Add entries to your daily Note with automatic timestamps.

### Usage

```bash
/auto-log Fixed authentication bug in production

/auto-log Deployed v2.1.0 to staging environment

/auto-log "Meeting notes: Q1 planning session
- Key decision: Focus on mobile
- Action: Update roadmap by Friday"
```

### How It Works

The owl:
1. Opens today's daily note (`YYYY-MM-DD.md`)
2. Finds the Log section
3. Adds your entry with timestamp (HH:MM format)
4. Appends to the bottom (chronological order)

### Example Output

```markdown
## Log

- 09:15 Fixed authentication bug in production
- 14:30 Deployed v2.1.0 to staging environment
- 16:45 Meeting notes: Q1 planning session
  - Key decision: Focus on mobile
  - Action: Update roadmap by Friday
```

*The wise owl always remembers when things happened!*

### Configuration

Daily note path is configured in `.Obsidian-scribe.json`:

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

## `/task-add` - Task Management

Create tasks with due dates in your daily note.

### Usage

```bash
/task-add Review PR #123 by tomorrow

/task-add Finish quarterly report by 2026-01-15

/task-add Call client about proposal by Friday
```

### How It Works

The owl:
1. Parses your task description and due date
2. Adds task to today's daily note
3. Uses Obsidian task format with due date metadata
4. Integrates with Dataview/Tasks plugins

### Example Output

```markdown
## Tasks

- [ ] Review PR #123 📅 2026-01-02
- [ ] Finish quarterly report 📅 2026-01-15
- [ ] Call client about proposal 📅 2026-01-03
```

*Never forget a deadline with the owl watching!*

## Session Start Hook

Runs automatically when you start Claude Code in your vault.

### What It Shows

```
Obsidian Scribe - Session started: 2026-01-01 05:57

Daily note: 2026-01-01.md exists
  Habits: 2/3 completed
  Food entries: 3
  Log entries: 8
Wikilink cache: 1154 entities

Recent achievements:
  2025: Phase 2 Complete: 9 components delivered
  2025: Configured WSL user level configs
  ...
```

### Benefits

- **Immediate context** - Know your vault status at a glance
- **Habit tracking** - See progress on daily habits
- **Cache status** - Wikilink entities are ready
- **Achievements** - Recent accomplishments surface automatically

*The owl greets you each morning with the state of your nest!* 🦉

## Common Workflows

### Morning Start Routine

```bash
# Start Claude Code (session hook shows status)
claude

# Plan your day
/task-add Complete feature X by EOD
/task-add Review documentation by 3pm

# Log first work
/auto-log Starting work on feature X
```

### Throughout the Day

```bash
# Log accomplishments as they happen
/auto-log Completed user authentication flow
/auto-log Fixed bug in payment processor
/auto-log Deployed v1.2.3 to production
```

### End of Day

```bash
# Final log entry
/auto-log End of day: shipped 3 features, closed 5 tickets

# Check achievements (if detected automatically)
# The achievement-detect hook may have already added them!
```

## Configuration Reference

### Daily Note Template

Create `templates/daily.md`:

```markdown
---
type: daily
date: {{date}}
tags:
  - "#daily"
---
# Habits
- [ ] Walk #habit
- [ ] Stretch #habit
- [ ] Vitamins #habit
---
# Food
-

---
# Today
## Tasks
## Log

```

### Config File `.obsidian-scribe.json`

```json
{
  "paths": {
    "daily_notes": "daily-notes",
    "templates": "templates"
  },
  "sections": {
    "log": "## Log",
    "tasks": "## Tasks",
    "food": "# Food"
  },
  "habits": [
    "Walk",
    "Stretch",
    "Vitamins"
  ]
}
```

## Troubleshooting

### "Daily note not found"

**Check:**
- Daily notes folder matches config (`daily-Notes/`)
- Today's note exists (create from template if needed)
- Path in config is relative to vault root

### Entries not appending

**Ensure:**
- Log section header matches config exactly (`## Log`)
- Section exists in daily note
- No structural issues (mismatched markdown)

### Session hook not showing

**Verify:**
- Python is installed and accessible as `Python` Command
- Hooks Are enabled in Plugin
- You're in your vault directory When starting Claude Code

## Related Features

- **[Achievements](achievements.md)** - Auto-detect significant accomplishments
- **[Rollup](rollup.md)** - Summarize daily logs into weekly/Monthly notes
- **[Examples: Daily Workflow](../examples/daily-workflow.md)** - See it All in Action

---

*"Every log entry is a feather in the owl's cap of Knowledge, dear scholar!"* 🦉📝
