# [[Example]]: [[Daily Workflow]] 🦉📅

*Hoot! Let the owl [[Show]] [[You]] a day in the life of a wise [[Knowledge]] worker.*

[[This]] example demonstrates how [[Obsidian Scribe]] fits into a typical workday.

## [[Morning]]: [[Session]] Start (8:30 [[AM]])

You open your [[Vault]] in [[Claude Code]]:

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
  2026-01-12: Completed Q1 planning documentation
```

*The owl shows you where you left off!* 🦉

## Planning Your Day (8:35 AM)

Add tasks for today:

```bash
/task-add Review PR #456 by 11am
/task-add Deploy hotfix to production by 2pm
/task-add Finish architecture doc by EOD
```

Your daily note now has:

```markdown
## Tasks
- [ ] Review PR #456 📅 2026-01-15 11:00
- [ ] Deploy hotfix to production 📅 2026-01-15 14:00
- [ ] Finish architecture doc 📅 2026-01-15 17:00
```

## Morning Work (9:00 AM)

Start your first task and log it:

```bash
/auto-log Starting PR review #456 - authentication refactor
```

Daily note log section:

```markdown
## Log
- 09:00 Starting PR review #456 - authentication refactor
```

## Mid-Morning Progress (10:30 AM)

You finish the review and provide feedback:

```bash
/auto-log **Completed PR review** - found 3 security issues, requested changes
```

*Notice the bold text - the owl knows this is important!*

The achievement-detect hook fires:

```
✓ Auto-Added 1 Achievement
--------------------------------------------------
  • **Completed PR review** - found 3 security issues, requested changes
--------------------------------------------------
Section: ### January 2026
```

Your Achievements.md automatically updated! 🏆

## Pre-Lunch Work (11:45 AM)

```bash
/auto-log Investigated database performance issue
/auto-log Identified query optimization - 80% improvement possible
```

## Lunch Break (12:00 PM)

Track your meal (if using food tracking):

```bash
/food Chicken salad with quinoa
/food Apple
```

## Afternoon: Critical Fix (2:15 PM)

Deploy that hotfix:

```bash
/auto-log Deployed hotfix v2.0.1 to production 🚀
/auto-log Verified fix - payment processing restored
/auto-log Zero downtime deployment ✅
```

The achievement hook detects multiple wins:

```
✓ Auto-Added 3 Achievements
--------------------------------------------------
  • Deployed hotfix v2.0.1 to production 🚀
  • Verified fix - payment processing restored
  • Zero downtime deployment ✅
--------------------------------------------------
```

*The owl celebrates your success!* 🦉🎉

## Late Afternoon: Documentation (4:30 PM)

```bash
/auto-log **Finished architecture documentation** for new microservices
/auto-log Updated diagrams with [[Mermaid]] syntax
```

Wikilink-suggest hook auto-applies brackets to "Mermaid" (it's a note in your vault).

## End of Day Review (5:15 PM)

Check vault health:

```bash
/vault-health
```

```
🦉 Vault Health Report

Notes: 1158 (+4 today)
Links: 3352 (+15 today)

Link Health:
  ✅ Well-connected: 895 notes (77%)
  ⚠️  Orphans: 42 notes (4%)

Your vault grew wiser today!
```

Final log entry:

```bash
/auto-log End of day: deployed hotfix, reviewed PR, completed docs ✅
```

## Evening: Rollup (7:00 PM)

It's Sunday, time for the weekly rollup:

```bash
/rollup-weekly 2026-W03
```

```
📊 Weekly Rollup: 2026-W03

Processing daily notes...
  ✓ 2026-01-13.md
  ✓ 2026-01-14.md
  ✓ 2026-01-15.md
  ...

Weekly summary generated: weekly-notes/2026-W03.md
```

Review the summary:

```markdown
# 2026-W03 Summary

## Key Achievements
- 🚀 Deployed hotfix v2.0.1 with zero downtime
- 🔒 Identified and fixed 3 security issues in auth system
- 📝 Completed architecture documentation for microservices
- 🎯 Maintained 77% vault connectivity

## Technical Work
- PR reviews: 3
- Deployments: 2 (1 planned, 1 hotfix)
- Documentation updates: 5 pages

## Metrics
- Daily log entries: 42
- Tasks completed: 18
- New notes created: 4

## Looking Ahead
- Continue microservices rollout
- Address remaining security audit items
```

*The owl weaves your daily threads into a coherent weekly tapestry!* 🦉

## What Happened Behind the Scenes

Throughout the day, hooks worked quietly:

1. **session-start** - Showed status at startup
2. **achievement-detect** - Captured 6 achievements
3. **wikilink-suggest** - Auto-linked "Mermaid" mention
4. **syntax-validate** - Checked for formatting issues

All automatic, all helpful, no manual work needed!

## Your Daily Note (Final State)

```markdown
---
type: daily
date: 2026-01-15
tags:
  - "#daily"
---
# Habits
- [x] Walk #habit
- [x] Stretch #habit
- [ ] Vitamins #habit
---
# Food
- Chicken salad with quinoa
- Apple
---
# Today
## Tasks
- [x] Review PR #456 📅 2026-01-15 11:00
- [x] Deploy hotfix to production 📅 2026-01-15 14:00
- [x] Finish architecture doc 📅 2026-01-15 17:00
## Log

- 09:00 Starting PR review #456 - authentication refactor
- 10:30 **Completed PR review** - found 3 security issues, requested changes
- 11:45 Investigated database performance issue
- 11:50 Identified query optimization - 80% improvement possible
- 14:15 Deployed hotfix v2.0.1 to production 🚀
- 14:20 Verified fix - payment processing restored
- 14:25 Zero downtime deployment ✅
- 16:30 **Finished architecture documentation** for new microservices
- 16:45 Updated diagrams with [[Mermaid]] syntax
- 17:15 End of day: deployed hotfix, reviewed PR, completed docs ✅
```

## Key Takeaways

1. **Start with session hook** - Know your vault status
2. **Log as you go** - Use `/[[Auto]]-[[Log]]` throughout the day
3. **Be descriptive** - Help the achievement detector succeed
4. **Use bold and emojis** - Signal important work
5. **End with rollup** - Summarize regularly

## Try It Yourself

Start tomorrow with:

```bash
# Morning
claude  # Session hook shows status
/task-add [your tasks]

# Throughout day
/auto-log [your accomplishments]

# Evening
/vault-health  # Check vault status
```

*Let the owl help you build a comprehensive record of your work, dear scholar!* 🦉📝
