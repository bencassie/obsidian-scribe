# [[Rollup]] Summarization 🦉📊

*Hoot! Watch the owl weave daily threads into the tapestry of time.*

The rollup [[System]] uses [[Multi]]-agent [[Orchestration]] to automatically summarize your [[Notes]] across time periods.

## The Rollup Chain

Daily → Weekly → [[Monthly]] → [[Quarterly]] → Yearly

[[Each]] level summarizes the previous, [[Creating]] progressively higher-level overviews.

## [[Features]]

| [[Feature]] | Type | Purpose |
|---------|------|---------|
| `/rollup` | [[Skill]] | Execute [[Full]] rollup chain |
| 5 Rollup Agents | Agents | [[Specialized]] summarization at each level |

**No [[MCP]] [[Required]]** - Works with your notes alone!

## How It Works

```mermaid
Daily Notes  →  Weekly Agent  →  Weekly Note
Weekly Notes →  Monthly Agent → Monthly Note
Monthly Notes → Quarterly Agent → Quarterly Note
Quarterly Notes → Yearly Agent → Yearly Note
```

Each agent:
1. Reads notes from the previous period
2. Extracts key achievements and patterns
3. Generates a structured summary
4. Writes to the target period note

*The owl sees patterns across time that humans might miss!* 🦉

## `/rollup` Command

Execute the complete rollup chain for the last 2 months.

### Usage

```bash
/rollup
```

### What It Does

1. **Daily → Weekly** - Last 8 weeks summarized
2. **Weekly → Monthly** - Last 2 months summarized
3. **Monthly → Quarterly** - Current quarter updated
4. **Quarterly → Yearly** - Current year updated

### Example Output

```
🦉 Rollup Chain Starting...

Daily → Weekly Summaries
  ✓ 2025-W52 complete
  ✓ 2026-W01 complete

Weekly → Monthly Summaries
  ✓ 2025-12 complete
  ✓ 2026-01 complete

Monthly → Quarterly Summary
  ✓ 2026-Q1 updated

Quarterly → Yearly Summary
  ✓ 2026 updated

Rollup Complete! Time to update achievements.
```

## Individual Rollup Agents

You can also run agents individually:

### Weekly Rollup

```bash
/rollup-weekly 2026-W01
```

Summarizes daily notes from that week into `weekly-notes/2026-W01.md`.

### Monthly Rollup

```bash
/rollup-monthly 2026-01
```

Summarizes weekly notes from that month into `monthly-notes/2026-01.md`.

### Quarterly Rollup

```bash
/rollup-quarterly 2026-Q1
```

Summarizes monthly notes from that quarter into `quarterly-notes/2026-Q1.md`.

### Yearly Rollup

```bash
/rollup-yearly 2026
```

Summarizes quarterly notes from that year into `yearly-notes/2026.md`.

## What Gets Summarized

Each agent extracts:

**Daily → Weekly:**
- Key accomplishments from log entries
- Completed tasks and milestones
- Technical work and deployments
- Meetings and decisions

**Weekly → Monthly:**
- Major achievements from each week
- Recurring themes and patterns
- Progress on ongoing projects
- Metrics and outcomes

**Monthly → Quarterly:**
- Monthly highlights and wins
- Quarterly goals progress
- Key metrics and KPIs
- Strategic decisions

**Quarterly → Yearly:**
- Quarterly achievements
- Year-over-year growth
- Major milestones
- Annual retrospective

*The owl distills wisdom from the noise of daily work!*

## Configuration

### Note Paths

Configure in `.obsidian-scribe.json`:

```json
{
  "paths": {
    "daily_notes": "daily-notes",
    "weekly_notes": "weekly-notes",
    "monthly_notes": "monthly-notes",
    "quarterly_notes": "quarterly-notes",
    "yearly_notes": "yearly-notes"
  }
}
```

### Templates

Create templates for each period type:

```
templates/
├── daily.md
├── weekly.md
├── monthly.md
├── quarterly.md
└── yearly.md
```

The agents use these to structure output.

## Common Workflows

### End of Week

```bash
# Summarize the week that just ended
/rollup-weekly 2026-W01
```

### End of Month

```bash
# Full chain to update everything
/rollup
```

### Quarterly Review

```bash
# Summarize the quarter
/rollup-quarterly 2026-Q1

# Then review quarterly-notes/2026-Q1.md
# Use insights to plan next quarter
```

### Annual Review

```bash
# End of year rollup
/rollup-yearly 2025

# Review yearly-notes/2025.md
# Celebrate wins, learn from challenges
```

## Example Weekly Summary

```markdown
# 2026-W01 Summary

## Overview
First week of 2026 focused on launching Q1 projects and setting up new infrastructure.

## Key Achievements
- 🚀 Deployed obsidian-scribe v1.0.7 with 100+ achievement patterns
- 📊 Completed vault health analysis (1154 notes, 95% link coverage)
- 🎯 Established cross-platform testing workflow (WSL + Windows)

## Technical Work
- Multi-platform plugin testing
- Achievement detection expansion
- Documentation overhaul with owl persona

## Metrics
- Daily log entries: 42
- Tasks completed: 15
- New notes created: 8

## Looking Ahead
- Continue documentation expansion
- Plan next plugin features
- Q1 goal tracking setup
```

*The owl transforms scattered entries into coherent narratives!* 🦉

## Best Practices

### 1. Run Rollups Regularly

- **Weekly:** Sunday evening or Monday morning
- **Monthly:** Last day or first day of month
- **Quarterly:** Last week of quarter
- **Yearly:** End of December

### 2. Review Before Finalizing

Agents are smart but not perfect:
- Read generated summaries
- Add context where needed
- Remove irrelevant items
- Highlight key wins

### 3. Use Summaries for Planning

Your past informs your future:
- Review monthly notes when planning quarters
- Check quarterly notes when setting annual goals
- Use yearly notes for retrospectives

## Troubleshooting

### "Note not found" errors

**Check:**
- Date format is correct (YYYY-WXX for weeks, YYYY-MM for months)
- Note exists in the configured folder
- Path in config matches actual folder names

### Agent hangs or times out

**Possible causes:**
- Too many notes to process (try smaller date ranges)
- Notes have complex formatting
- System resources constrained

**Solutions:**
- Run individual agents instead of full `/rollup`
- Split large periods into smaller chunks
- Increase agent timeout in [[Config]]

### Summaries [[Are]] too generic

**[[Improve]] input:**
- Write detailed daily [[Log]] entries
- [[Use]] [[Achievement]]-detect [[Hook]] for [[Auto]]-tracking
- Add [[Context]] to significant work

The owl can [[Only]] summarize [[What]] [[You]]'ve captured!

## [[Related]] Features

- **[Daily Logging](daily-logging.md)** - Capture work that rollup summarizes
- **[Achievements](achievements.md)** - Significant accomplishments [[Surface]] in summaries
- **[Examples: Rollup Chain](../examples/rollup-chain.md)** - Step-by-step walkthrough

---

*"Time [[Reveals]] patterns [[Invisible]] in the [[Moment]]. Let the owl [[Show]] you the way, dear scholar!"* 🦉📊
