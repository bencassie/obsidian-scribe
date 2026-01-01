# Example: Vault Analysis 🦉🔍

*Hoot! Let the owl Guide You through a Complete vault health check and Optimization Session.*

This example Shows how to Use Vault Intelligence Skills to Analyze, diagnose, and Improve your Obsidian vault.

## Prerequisites

- smoking-Mirror MCP Server configured ([setup guide](../installation/mcp-servers.md))
- A vault with Some Notes (works Best with 100+ notes)

## Scenario

You haven't reviewed your vault structure in months. Time for a Deep analysis!

## Step 1: Overall Health Check (10 min)

Start with the comprehensive health Report:

```bash
/vault-health
```

**Output:**

```
🦉 Vault Health Report

📊 Overview
Notes: 1154
Links: 3337 (2.89 avg per note)
Tags: 287 unique
Folders: 12

🔗 Link Health
  ✅ Well-connected: 892 notes (77%)
  ⚠️  Orphans: 45 notes (4%)
  🌟 Hubs: 12 notes (1%)
  🎯 Dead-ends: 28 notes (2%)

📁 Folder Distribution
  tech/: 412 notes (36%)
  personal/: 234 notes (20%)
  work/: 156 notes (14%)
  daily-notes/: 298 notes (26%)

🔍 Top Gaps
  1. "Machine Learning" - mentioned 23 times, no note
  2. "API Design" - mentioned 15 times, no note
  3. "Database Optimization" - mentioned 12 times, no note

💡 Recommendations
  - Link orphan notes (45 to review)
  - Create notes for knowledge gaps (3 topics)
  - Consider archiving stale content
```

**Analysis:**
- Overall health is good (77% well-connected)
- Some cleanup needed (45 orphans)
- Knowledge gaps identified (3 missing topics)

*The owl has spoken - let's address these issues!* 🦉

## Step 2: Fix Broken Links (5 min)

Before anything else, repair broken wikilinks:

```bash
/vault-fix-links
```

**Output:**

```
🦉 Scanning for broken links...

Broken Links Found:

tech/tools/Obsidian.md
  Line 42: Claude → Claude Code? ✓ Fixed
  Line 58: MCP → Model Context Protocol? ✓ Fixed

daily-notes/2025-12-15.md
  Line 23: React Hooks → React/Hooks? ✓ Fixed

3 broken links repaired automatically
```

*Magnificent! The vault's neural pathways are now clear.*

## Step 3: Address Orphan Notes (15 min)

Find isolated notes:

```bash
/vault-orphans
```

**Output:**

```
🦉 Orphan Notes (No Backlinks)

personal/ideas/random-thought.md
  Created: 2025-08-15
  Tags: #idea

tech/drafts/unfinished-article.md
  Created: 2025-06-20
  Tags: #draft, #tech

work/archive/old-project-notes.md
  Created: 2024-11-10
  Tags: #work, #archived

... (42 more)
```

**Decision Matrix:**

| Note Type | Action |
|-----------|--------|
| Recent ideas | Link from related notes |
| Old drafts | Archive or delete |
| Project notes | Archive if complete |

**Example actions:**

```bash
# Link a recent idea
# (Open in Obsidian and add backlinks from related notes)

# Move old content to archive
mv work/archive/old-project-notes.md .archive/2024/

# Delete truly orphaned drafts
# (After reviewing content)
```

*15 orphans linked, 18 archived, 12 deleted. Progress!*

## Step 4: Find Hub Notes (5 min)

Identify your most connected notes:

```bash
/vault-hubs
```

**Output:**

```
🦉 Hub Notes (Highly Connected)

tech/Index.md
  Backlinks: 45
  Outlinks: 67
  Total connections: 112

work/Projects.md
  Backlinks: 38
  Outlinks: 42
  Total connections: 80

personal/goals/Annual-Review.md
  Backlinks: 28
  Outlinks: 35
  Total connections: 63
```

**Insights:**
- tech/Index.md is your technical knowledge hub
- work/Projects.md tracks active work
- Annual-Review connects personal goals

*These are your vault's cornerstones!*

## Step 5: Discover Clusters (10 min)

Find groups of related notes:

```bash
/vault-clusters
```

**Output:**

```
🦉 Knowledge Clusters Detected

Cluster 1: Web Development (45 notes)
  Core: tech/web/, tech/frameworks/
  Hub: tech/frameworks/React.md
  Topics: React, TypeScript, API design

Cluster 2: Personal Development (32 notes)
  Core: personal/goals/, personal/learning/
  Hub: personal/goals/Annual-Review.md
  Topics: Career, Skills, Health

Cluster 3: Work Projects (28 notes)
  Core: work/projects/, work/meetings/
  Hub: work/Projects.md
  Topics: Current work, Team, Clients
```

**Observation:**
Your vault naturally organizes into 3 major domains - this mirrors your mental model!

## Step 6: Fill Knowledge Gaps (20 min)

Create missing notes:

```bash
/vault-gaps
```

```
🦉 Knowledge Gaps

"Machine Learning" - mentioned 23 times
  tech/ai/neural-networks.md (5 mentions)
  tech/tools/Python.md (4 mentions)
  daily-notes/2025-12/*.md (14 mentions)

Suggested: Create tech/ai/Machine-Learning.md
```

**Create the note** (in Obsidian):

```markdown
# Machine Learning

## Overview
[Add content based on your knowledge/research]

## Applications
- Neural networks
- Python libraries
- Real-world use cases

## Related
- Artificial Intelligence
- Data Science
- Python
```

Repeat for other gaps: API Design, Database Optimization.

*The owl's nest of knowledge grows more complete!* 🦉

## Step 7: Link Density Analysis (5 min)

Check which areas need more connections:

```bash
/vault-link-density
```

**Output:**

```
📊 Link Density by Folder

High Density (Good):
  tech/frameworks/: 4.2 links/note
  personal/goals/: 3.8 links/note

Medium Density:
  work/projects/: 2.1 links/note
  daily-notes/: 1.8 links/note

Low Density (Needs Work):
  tech/drafts/: 0.6 links/note ⚠️
  work/archive/: 0.3 links/note ⚠️
```

**Action:** Focus linking efforts on tech/drafts/ - these notes need context!

## Step 8: Find Stale Content (10 min)

Identify neglected but important notes:

```bash
/vault-stale
```

**Output:**

```
🦉 Stale Important Notes

tech/frameworks/React.md
  Last modified: 180 days ago
  Backlinks: 23
  Importance: HIGH

work/processes/Code-Review.md
  Last modified: 90 days ago
  Backlinks: 15
  Importance: MEDIUM
```

**Action:** Update React.md with recent learnings, verify Code-Review.md is still current.

## Step 9: Check Folder Organization (5 min)

Review folder structure:

```bash
/vault-folder-health
```

**Output:**

```
📁 Folder Health

tech/ (412 notes)
  ⚠️  78 notes directly in tech/ (consider subfolders)
  Suggested structure:
    tech/languages/
    tech/tools/
    tech/concepts/

personal/ (234 notes)
  ✅ Well organized with subfolders
  Subfolders: goals/, health/, journal/, learning/

work/ (156 notes)
  ✅ Good subfolder usage
  Subfolders: projects/, meetings/, processes/
```

**Action:** Reorganize tech/ folder - move 78 loose notes into subfolders.

## Step 10: Final Health Check (5 min)

Re-run health check to see improvements:

```bash
/vault-health
```

**Output:**

```
🦉 Vault Health Report (After Optimization)

Notes: 1157 (+3 new)
Links: 3398 (+61 new links)

Link Health:
  ✅ Well-connected: 935 notes (81%) ⬆️ +4%
  ✅ Orphans: 27 notes (2%) ⬇️ -2%
  🌟 Hubs: 12 notes (1%)

Knowledge Gaps: 0 (was 3) ✅

Your vault is now wiser!
```

**Improvements:**
- Well-connected notes: 77% → 81%
- Orphans: 45 → 27 (18 addressed)
- Knowledge gaps: 3 → 0 (all filled)
- Total links: +61

*The owl is pleased with your tending of the knowledge garden!* 🦉✨

## Summary: 90-Minute Vault Optimization

| Step | Time | Impact |
|------|------|--------|
| Health check | 10 min | Baseline |
| Fix broken links | 5 min | 3 repairs |
| Address orphans | 15 min | 18 linked/archived |
| Find hubs | 5 min | Identify key notes |
| Discover clusters | 10 min | Understand structure |
| Fill gaps | 20 min | 3 new notes |
| Link density | 5 min | Focus areas |
| Update stale | 10 min | 2 notes refreshed |
| Folder health | 5 min | Reorganization plan |
| Final check | 5 min | Measure progress |

**Total:** 90 minutes for significant vault improvement!

## Monthly Maintenance Routine

Run this workflow monthly:

1. `/vault-health` - Baseline
2. `/vault-fix-Links` - Clean up
3. `/vault-Orphans` - Link or archive
4. `/vault-gaps` - Fill missing topics
5. `/vault-stale` - Update important notes
6. `/vault-health` - Measure improvement

*Even the wisest vaults Need regular tending!*

## Related Resources

- **[Vault Intelligence Features](../features/vault-intelligence.md)** - All 15 skills
- **[Installation: MCP Servers](../installation/mcp-servers.md)** - Setup smoking-mirror
- **[Daily Workflow](daily-workflow.md)** - Ongoing Maintenance

---

*"A well-tended vault is a joy to Explore, dear scholar. Let the owl help you keep it that way!"* 🦉🔍
