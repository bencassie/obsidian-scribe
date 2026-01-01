# Skills Reference

Complete reference for all 21 skills, 4 hooks, and 5 agents in Obsidian Scribe.

---

## Daily Capture

### `/auto-log`

Add timestamped entries to your daily note.

```bash
/auto-log Fixed authentication bug in production
/auto-log "Meeting notes: Q1 planning session
- Key decision: Focus on mobile
- Action: Update roadmap by Friday"
```

**Output in daily note:**
```markdown
## Log
- 09:15 Fixed authentication bug in production
- 14:30 Meeting notes: Q1 planning session
  - Key decision: Focus on mobile
  - Action: Update roadmap by Friday
```

### `/task-add`

Create tasks with natural language due dates.

```bash
/task-add Review PR #123 by tomorrow
/task-add Finish quarterly report by 2026-01-15
/task-add Call client about proposal by Friday
```

**Output:**
```markdown
## Tasks
- [ ] Review PR #123 📅 2026-01-02
- [ ] Finish quarterly report 📅 2026-01-15
- [ ] Call client about proposal 📅 2026-01-03
```

### `/food`

Log food entries to your daily note.

```bash
/food Chicken salad with quinoa
```

---

## Vault Intelligence

**Requires:** [smoking-mirror MCP](installation/mcp-servers.md)

### `/vault-health`

Comprehensive vault diagnostics.

```bash
/vault-health
```

**Shows:** Total notes, links, tags, orphan rate, hubs, link density, knowledge gaps.

### `/vault-stats`

Quick statistics without analysis.

```bash
/vault-stats
```

### `/vault-orphans`

Find notes with no backlinks.

```bash
/vault-orphans
```

### `/vault-hubs`

Find highly-connected notes.

```bash
/vault-hubs
```

### `/vault-clusters`

Detect topic clusters in your vault.

```bash
/vault-clusters
```

### `/vault-gaps`

Find mentioned but undocumented topics.

```bash
/vault-gaps
```

**Example output:**
```
🦉 Knowledge Gaps Detected

"API Authentication" - mentioned 12 times, no note
"Database Optimization" - mentioned 8 times, no note
```

### `/vault-stale`

Find important notes not updated recently.

```bash
/vault-stale
```

### `/vault-dead-ends`

Find notes with backlinks but no outgoing links.

```bash
/vault-dead-ends
```

### `/vault-backlinks`

Show all notes linking to a specific note.

```bash
/vault-backlinks "Note Name"
```

### `/vault-related`

Find notes similar to the current note.

```bash
/vault-related "Current Note"
```

### `/vault-fix-links`

Find and repair broken wikilinks.

```bash
/vault-fix-links
```

### `/vault-unlinked-mentions`

Find unlinked mentions of a term.

```bash
/vault-unlinked-mentions "Entity Name"
```

### `/vault-link-density`

Analyze link density patterns.

```bash
/vault-link-density
```

### `/vault-folder-health`

Check folder organization.

```bash
/vault-folder-health
```

### `/vault-search`

Advanced search with filters.

```bash
/vault-search --folder tech --tags work,important
```

---

## Wikilink Automation

### `/rebuild-wikilink-cache`

Rebuild the entity cache from your vault.

```bash
/rebuild-wikilink-cache
```

**When to use:**
- After creating many new notes
- After renaming notes
- When suggestions seem outdated

### `/wikilink-apply`

Apply wikilink suggestions to a note.

```bash
/wikilink-apply path/to/note.md
```

**Requires:** smoking-mirror MCP

---

## Periodic Rollups

### `/rollup`

Execute the complete rollup chain for the last 2 months.

```bash
/rollup
```

**What it does:**
1. Daily → Weekly (last 8 weeks)
2. Weekly → Monthly (last 2 months)
3. Monthly → Quarterly (current quarter)
4. Quarterly → Yearly (current year)

### `/rollup-weekly`

Summarize a specific week.

```bash
/rollup-weekly 2026-W01
```

Creates `weekly-notes/2026-W01.md` from daily notes.

### `/rollup-monthly`

Summarize a specific month.

```bash
/rollup-monthly 2026-01
```

Creates `monthly-notes/2026-01.md` from weekly notes.

### `/rollup-quarterly`

Summarize a specific quarter.

```bash
/rollup-quarterly 2026-Q1
```

Creates `quarterly-notes/2026-Q1.md` from monthly notes.

### `/rollup-yearly`

Summarize a specific year.

```bash
/rollup-yearly 2026
```

Creates `yearly-notes/2026.md` from quarterly notes.

---

## Hooks

Hooks run automatically - no commands needed.

### `session-start`

**Trigger:** When Claude Code starts in your vault

**Shows:**
- Daily note status
- Habit progress
- Wikilink cache count
- Recent achievements

### `achievement-detect`

**Trigger:** After editing daily notes

**Detects 126 patterns** across 12 categories:
- Actions: Built, created, deployed, fixed, shipped
- Progress: Completed, finished, launched
- Success: Works, passed, all tests green
- Milestones: v1.0, first time, breakthrough
- Bold text: `**Anything in bold**`
- Emojis: ✅ 🎉 🚀 💪 🏆

**Output:** Auto-adds to `Achievements.md`

### `wikilink-suggest`

**Trigger:** After Edit/Write operations

Auto-applies `[[wikilinks]]` to known entities in your notes.

### `syntax-validate`

**Trigger:** After Edit/Write operations

Warns about:
- Wrapped wikilinks (`**[[Link]]**`)
- Angle brackets that break links (`ILogger<T>`)
- Wikilinks in frontmatter

---

## Agents

5 specialized agents for rollup summarization:

| Agent | Source | Output |
|-------|--------|--------|
| Weekly Agent | Daily notes | Weekly summary |
| Monthly Agent | Weekly notes | Monthly summary |
| Quarterly Agent | Monthly notes | Quarterly summary |
| Yearly Agent | Quarterly notes | Yearly summary |
| Rollup Agent | Orchestrates all agents | Full chain |

---

## Configuration

All paths are configured in `.obsidian-scribe.json`:

```json
{
  "paths": {
    "daily_notes": "daily-notes",
    "weekly_notes": "weekly-notes",
    "monthly_notes": "monthly-notes",
    "quarterly_notes": "quarterly-notes",
    "yearly_notes": "yearly-notes",
    "achievements": "personal/goals/Achievements.md",
    "templates": "templates"
  },
  "sections": {
    "log": "## Log",
    "tasks": "## Tasks",
    "food": "# Food"
  },
  "wikilinks": {
    "auto_apply": true,
    "min_entity_length": 3,
    "exclude_patterns": ["the", "and", "or", "but"]
  }
}
```

---

## Dependencies

| Feature | Requires |
|---------|----------|
| All hooks | Python 3.8+ |
| 15 vault-* skills | smoking-mirror MCP |
| `/wikilink-apply` | smoking-mirror MCP |
| Other skills | None (works out of box) |

---

## Related

- [Workflows](workflows.md) — Real examples
- [Comparison](comparison.md) — vs other tools
- [MCP Setup](installation/mcp-servers.md) — Enable vault intelligence
