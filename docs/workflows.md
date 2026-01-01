# Workflows

Real examples of how Obsidian Scribe fits into your work.

---

## Daily Workflow

A typical workday with Obsidian Scribe.

### Morning Start (8:30 AM)

```bash
cd ~/obsidian/vault
claude
```

The session-start hook greets you:

```
Obsidian Scribe - Session started: 2026-01-15 08:30

Daily note: 2026-01-15.md exists
  Habits: 0/3 completed
  Food entries: 0
  Log entries: 0
Wikilink cache: 1154 entities

Recent achievements:
  2026-01-14: Deployed authentication system v2.0
  2026-01-13: Fixed critical payment bug
```

### Plan Your Day

```bash
/task-add Review PR #456 by 11am
/task-add Deploy hotfix to production by 2pm
/task-add Finish architecture doc by EOD
```

### Log As You Work

```bash
/auto-log Starting PR review #456 - authentication refactor
```

```bash
/auto-log **Completed PR review** - found 3 security issues, requested changes
```

The achievement hook fires automatically:

```
✓ Auto-Added 1 Achievement
--------------------------------------------------
  • **Completed PR review** - found 3 security issues, requested changes
--------------------------------------------------
```

### Deploy Something

```bash
/auto-log Deployed hotfix v2.0.1 to production 🚀
/auto-log Verified fix - payment processing restored
/auto-log Zero downtime deployment ✅
```

All three entries get added to Achievements.md.

### End of Day

```bash
/vault-health
```

```
🦉 Vault Health Report

Notes: 1158 (+4 today)
Links: 3352 (+15 today)

Your vault grew wiser today!
```

---

## Weekly Rollup

Run every Sunday evening:

```bash
/rollup-weekly 2026-W03
```

**Output:**

```
📊 Weekly Rollup: 2026-W03

Processing daily notes...
  ✓ 2026-01-13.md
  ✓ 2026-01-14.md
  ✓ 2026-01-15.md
  ...

Weekly summary generated: weekly-notes/2026-W03.md
```

**Generated summary:**

```markdown
# 2026-W03 Summary

## Key Achievements
- 🚀 Deployed hotfix v2.0.1 with zero downtime
- 🔒 Identified and fixed 3 security issues in auth system
- 📝 Completed architecture documentation for microservices

## Technical Work
- PR reviews: 3
- Deployments: 2 (1 planned, 1 hotfix)
- Documentation updates: 5 pages

## Metrics
- Daily log entries: 42
- Tasks completed: 18
- New notes created: 4
```

---

## The Complete Rollup Chain

Run the full chain at month end:

```bash
/rollup
```

This executes:
1. **Daily → Weekly** — Last 8 weeks summarized
2. **Weekly → Monthly** — Last 2 months summarized
3. **Monthly → Quarterly** — Current quarter updated
4. **Quarterly → Yearly** — Current year updated

All in about 60 seconds.

### Individual Rollups

```bash
/rollup-weekly 2026-W01     # Specific week
/rollup-monthly 2026-01     # Specific month
/rollup-quarterly 2026-Q1   # Specific quarter
/rollup-yearly 2026         # Specific year
```

---

## Vault Maintenance

Run monthly to keep your vault healthy.

### Health Check

```bash
/vault-health
```

```
🦉 Vault Health Report

Notes: 1154
Links: 3337 (2.89 avg per note)
Tags: 287 unique

Link Health:
  ✅ Well-connected: 892 notes (77%)
  ⚠️  Orphans: 45 notes (4%)
  🌟 Hubs: 12 notes (1%)

Top Gaps:
  - "Machine Learning" mentioned 23 times, no note
  - "API Design" mentioned 15 times, no note
```

### Fix Issues

```bash
/vault-orphans        # Find isolated notes
/vault-fix-links      # Repair broken links
/vault-gaps           # Find undocumented topics
```

### Optimize Structure

```bash
/vault-folder-health  # Check organization
/vault-clusters       # Find topic groups
/vault-stale          # Find neglected notes
```

---

## Research Session

Starting research on a new topic:

```bash
# What do I already know?
/vault-search --tags research
/vault-related "Machine Learning"

# What's missing?
/vault-gaps

# Find background material
/vault-backlinks "Python"
/vault-hubs
```

---

## Performance Review Prep

Your Achievements.md has been auto-populated all quarter:

```bash
# Review the quarter
cat personal/goals/Achievements.md

# Get high-level summary
/rollup-quarterly 2026-Q1
```

The quarterly summary includes:
- OKR progress
- Major milestones
- Team collaboration metrics
- Key challenges and learnings

---

## Wikilink Cleanup

After adding many new notes:

```bash
# Rebuild the entity cache
/rebuild-wikilink-cache

# Find and fix broken links
/vault-fix-links

# Find unlinked mentions
/vault-unlinked-mentions "Claude Code"
```

---

## Best Practices

### 1. Log Descriptively

**Good (detected as achievement):**
```bash
/auto-log Built complete user authentication system with OAuth
```

**Too vague (missed):**
```bash
/auto-log Worked on stuff
```

### 2. Use Bold and Emojis

```bash
/auto-log **Launched new feature** - 1000+ users already 🚀
```

Bold text and emojis signal importance to the achievement hook.

### 3. Run Rollups on Schedule

| Period | When to Run |
|--------|-------------|
| Weekly | Sunday evening |
| Monthly | Last day of month |
| Quarterly | Last week of quarter |
| Yearly | End of December |

### 4. Review Generated Summaries

Agents are smart but not perfect:
- Read generated summaries
- Add missing context
- Remove irrelevant items
- Highlight key wins

---

## Related

- [Skills Reference](skills-reference.md) — All commands
- [MCP Setup](installation/mcp-servers.md) — Enable vault intelligence
