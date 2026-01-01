# Achievements 🦉🏆

*Hoot! Let the owl celebrate your victories, Both great and small.*

The Achievement Detection System automatically identifies and tracks significant accomplishments from your daily work.

## Features

| Feature | Type | Purpose |
|---------|------|---------|
| `achievement-detect` | Hook | Auto-detect achievements from Daily Notes |

**No MCP Required** - Works with daily Notes alone!

## How It Works

The achievement detection hook:
1. Runs automatically After You Edit daily notes
2. Scans Log entries for achievement patterns
3. Auto-adds up to 3 achievements to your Achievements file
4. Deduplicates to avoid repeats

*The owl notices your Wins even When you're too modest to claim them!* 🦉

## What Gets Detected

The owl watches for **126 patterns** across 12 categories:

### 1. Simple Actions
- Built, Created, tested, configured
- Fixed, Updated, deployed
- Automated, scripted

### 2. Learning & Discovery
- Learned, figured out
- Discovered, understood
- Researched, explored

### 3. Problem Solving
- Solved, debugged
- Diagnosed, Identified
- Worked around

### 4. Communication
- Presented, Documented
- Reviewed, Merged
- Shared, published

### 5. Progress Indicators
- Finished, Completed
- Shipped, released
- Wrapped up, closed out

### 6. Success Signals
- Works, passed, green
- Successful, succeeded
- All tests pass

### 7. Milestones
- First time, finally
- Breakthrough
- Version numbers (v1.0.2)

### 8. Bold Text
- **Anything in bold** = important!

### 9. Work Items
- Closed Ticket, PR merged
- OC123456 (ticket numbers)

### 10. Meta Achievements
- Achieved, Accomplished
- Nailed, crushed

### 11. Emojis
- ✅ 🎉 🚀 💪 🏆 🔥 ✨ 👍 🎯

### 12. Late Night Work
- Timestamps 22:00-05:00 (dedication!)

## Example Detection

**You write in daily Note:**
```markdown
## Log

- 09:15 Fixed critical authentication bug in production
- 14:30 **Launched v2.1.0** to all users 🚀
- 18:45 Successfully migrated database to new infrastructure
- 23:30 Finished documentation overhaul
```

**The owl automatically adds to Achievements.md:**
```markdown
### January 2026

- Fixed critical authentication bug in production
- **Launched v2.1.0** to all users 🚀
- Successfully migrated database to new infrastructure
```

*(Note: Only top 3 per edit, and that late-night work got counted!)*

## Configuration

### Achievements File Path

Set in `.obsidian-scribe.json`:

```json
{
  "paths": {
    "achievements": "personal/goals/Achievements.md"
  }
}
```

### Achievement File Structure

```markdown
# Achievements

## 2026

### January 2026
- First achievement here
- Second achievement here

### February 2026
- Another month's wins

## 2025

### December 2025
- Previous achievements
```

The owl automatically:
- Creates new month sections as needed
- Places achievements in current month
- Maintains chronological order

## How to Capture Achievements

### Write Descriptive Log Entries

**Good (detected):**
```markdown
- 10:30 Built complete user authentication system with OAuth
- 14:00 Deployed v1.2.0 to production - zero downtime
- 16:45 Fixed critical payment processing bug
```

**Too vague (missed):**
```markdown
- 10:30 Worked on stuff
- 14:00 Did some deployment
- 16:45 Bug fix
```

*Be specific! The owl can only celebrate wins you describe clearly.*

### Use Bold for Emphasis

```markdown
- 11:00 **Launched new feature** - 1000+ users already
```

The owl knows bold = important!

### Use Achievement Emojis

```markdown
- 15:30 Shipped Q4 roadmap deliverables ✅
- 17:00 Hit 10,000 users milestone 🎉
- 19:00 Deployed infrastructure upgrade 🚀
```

### Celebrate Small Wins

The owl detects:
```markdown
- Learned new framework
- Figured out complex bug
- Tested cross-platform setup
```

Don't wait for huge milestones - progress is achievement!

## Viewing Achievements

Your achievements file tracks your career:

```bash
# View in Obsidian or any markdown editor
cat personal/goals/Achievements.md
```

**Use for:**
- Performance reviews
- Resume updates
- Weekly retrospectives
- Quarterly planning
- Annual reflections

## Liberal Detection Philosophy

The owl uses a **"capture more, curate later"** approach:

- ✅ Better to catch too much than miss wins
- ✅ Easy to remove false positives manually
- ✅ 126 patterns cover most work types
- ✅ You decide what makes the final cut

*Let the owl err on the side of celebration!* 🦉🎉

## Deduplication

The owl is smart about duplicates:

**Normalizes text:**
- Removes timestamps (10:30)
- Removes bold/italic markers
- Removes wikilink brackets
- Compares first 60 characters

**Example:**
```markdown
- 10:30 **Built** authentication system
- Built authentication system
```

These are treated as the same achievement (won't duplicate).

## Hook Notifications

When achievements are detected, you'll see:

```
✓ Auto-Added 2 Achievements
--------------------------------------------------
  • Fixed critical bug in payment processor
  • Deployed v1.2.0 to production with zero downtime
--------------------------------------------------
Section: ### January 2026
```

*The owl proudly announces your wins!*

## Common Workflows

### Daily Review

```markdown
# At end of day
- 17:00 Reviewed today's work - shipped 3 features ✅
```

The hook fires and adds to Achievements.md automatically.

### Weekly Retrospective

1. Check daily notes for the week
2. Achievement hook has been capturing wins
3. Review Achievements.md
4. Keep important ones, remove noise
5. Use in weekly rollup

### Monthly/Quarterly Reviews

Your Achievements file is pre-populated with wins:
- Review month/quarter achievements
- Highlight top 5-10 for summaries
- Use in performance reviews
- Update resume/portfolio

## Customization

### Add Custom Patterns

*Coming soon: Configurable patterns in `.obsidian-scribe.json`*

Current patterns are in:
```
plugins/obsidian-scribe/hooks/achievement-detect.py
```

### Adjust Sensitivity

The 126 patterns are intentionally liberal. To reduce noise:
- Be more selective in log entries
- Review and curate Achievements.md weekly
- Remove patterns from hook code (advanced)

## Troubleshooting

### Achievements not detecting

**Check:**
- You're editing daily notes (not other files)
- Log entries use achievement keywords
- Hook is enabled in plugin config
- Python is available as `Python` Command

### Too many false Positives

**Solutions:**
- Be more Specific in log entries
- Use bold/emojis intentionally
- Review Achievements.md weekly to prune
- Increase minimum text length in hook Config

### Missing obvious achievements

**Ensure you're Using trigger words:**
- Action verbs: built, created, deployed, fixed
- Success words: works, passed, successful
- Bold text for important items
- Emojis for celebrations

## Related Features

- **[Daily Logging](daily-logging.md)** - Capture work that becomes achievements
- **[Rollup](rollup.md)** - Achievements Surface in period summaries
- **[Examples: Daily Workflow](../examples/daily-workflow.md)** - See it in action

---

*"Every achievement, great or small, is a feather in your cap of wisdom, dear scholar. Let the owl help you celebrate them all!"* 🦉🏆
