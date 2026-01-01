# [[Vault Intelligence]] 🦉🧠

*Hoot! The owl sees your [[Knowledge]] [[Graph]] in [[All]] its interconnected glory.*

[[Vault]] [[Intelligence]] [[Features]] [[Analyze]] your [[Note]] network to find patterns, gaps, and [[Optimization]] [[Opportunities]].

## Prerequisites

**Requires:** smoking-[[Mirror]] [[MCP]] [[Server]] ([setup guide](../installation/mcp-servers.md))

Without it, [[These]] 15 [[Skills]] won't work. [[But]] [[When]] configured - *the owl's eyes truly open!* 🦉

## [[Overview]] Skills

### `/vault-health`

Comprehensive vault diagnostics and health [[Report]].

```bash
/vault-health
```

**Shows:**
- Total notes, links, tags
- Orphan rate (isolated notes)
- Hub notes (highly connected)
- Link density patterns
- Folder organization stats
- Knowledge gaps

**Example Output:**
```
🦉 Vault Health Report

Notes: 1154
Links: 3337 (2.89 avg per note)
Tags: 287 unique
Folders: 12

Link Health:
  ✅ Well-connected: 892 notes (77%)
  ⚠️  Orphans: 45 notes (4%)
  🌟 Hubs: 12 notes (1%)

Top Gaps:
  - "Machine Learning" mentioned 23 times, not documented
  - "API Design" mentioned 15 times, no dedicated note
```

*A single command reveals the state of your knowledge nest!*

### `/vault-stats`

Quick statistics without analysis.

```bash
/vault-stats
```

**Shows:**
- Note count
- Link metrics
- Tag usage
- Folder distribution

## Connection Analysis

### `/vault-backlinks`

Show all notes that link TO a specific note.

```bash
/vault-backlinks "Note Name"
```

**Example:**
```
Backlinks to "Claude Code"

tech/tools/Obsidian.md (line 42)
  ...using Claude Code for automation...

daily-notes/2026-01-01.md (line 35)
  ...tested Claude Code integration...

3 total backlinks found
```

*The owl knows who references whom!*

### `/vault-bidirectional`

Find notes that link to each other (mutual connections).

```bash
/vault-bidirectional
```

Strong bidirectional links indicate related concepts worth merging or cross-referencing.

### `/vault-[[Related]]`

Find notes similar to the current note (by tags, folder, keywords).

```bash
/vault-related "Current Note"
```

### `/vault-suggest`

Get wikilink suggestions for a note using smoking-mirror entity detection.

```bash
/vault-suggest path/to/note.md
```

## Problem Detection

### `/vault-[[Orphans]]`

Find notes with no backlinks (isolated in the graph).

```bash
/vault-orphans
```

**Example Output:**
```
🦉 Orphan Notes Found

personal/ideas/random-thought.md
tech/drafts/unfinished-article.md
work/archive/old-project-notes.md

45 orphan notes total

Consider:
- Linking from related notes
- Moving to archive
- Deleting if no longer relevant
```

*Every note deserves at least one connection!*

### `/vault-dead-ends`

Find notes with backlinks but no outgoing links.

```bash
/vault-dead-ends
```

These notes consume knowledge but don't contribute - consider adding links out.

### `/vault-stale`

Find important notes (many backlinks) not modified recently.

```bash
/vault-stale
```

**Example:**
```
Stale Important Notes

tech/frameworks/React.md
  Last modified: 180 days ago
  Backlinks: 23

work/processes/Code-Review.md
  Last modified: 90 days ago
  Backlinks: 15
```

*Even wisdom grows old without tending!*

### `/vault-gaps`

Find knowledge gaps - topics mentioned but not documented.

```bash
/vault-gaps
```

**Example:**
```
🦉 Knowledge Gaps Detected

"API Authentication" - mentioned 12 times, no note
"Database Optimization" - mentioned 8 times, no note
"Testing Strategy" - mentioned 6 times, no note

Consider creating notes for these topics!
```

## Network Topology

### `/vault-[[Hubs]]`

Find highly connected notes (many links in/out).

```bash
/vault-hubs
```

Hubs are central to your knowledge graph - index pages, concept notes, or frequently referenced topics.

### `/vault-[[Clusters]]`

Find groups of highly connected notes.

```bash
/vault-clusters
```

Clusters reveal natural topic areas in your vault.

### `/vault-[[Link]]-density`

Analyze link density patterns across vault.

```bash
/vault-link-density
```

Shows which folders/topics are well-connected vs. isolated.

## Maintenance Tools

### `/vault-fix-[[Links]]`

Find and repair broken wikilinks.

```bash
/vault-fix-links
```

**Example:**
```
🦉 Broken Links Found

tech/tools/Obsidian.md
  [[Claude]] → Did you mean [[Claude Code]]?
  [[MCP]] → Did you mean [[Model Context Protocol]]?

2 broken links repaired
```

### `/vault-unlinked-mentions`

Find places where an entity is mentioned but not wikilinked.

```bash
/vault-unlinked-mentions "Entity Name"
```

**Example:**
```
Unlinked Mentions of "Obsidian"

daily-notes/2025-12-30.md (line 15)
  ...using Obsidian for notes...
  Suggestion: ...using [[Obsidian]] for notes...

tech/tools/PKM.md (line 42)
  ...Obsidian is a powerful tool...
  Suggestion: ...[[Obsidian]] is a powerful tool...

8 unlinked mentions found
```

### `/vault-[[Search]]`

Advanced search with filters (folder, tags, frontmatter).

```bash
/vault-search --folder tech --tags work,important
```

## Organization Analysis

### `/vault-folder-health`

Analyze vault organization by folder structure.

```bash
/vault-folder-health
```

**Example:**
```
📊 Folder Health Analysis

personal/ (234 notes)
  Subfolders: goals/, health/, journal/
  Well organized ✅

tech/ (412 notes)
  ⚠️  78 notes directly in tech/ (consider subfolders)
  Suggested: tech/languages/, tech/tools/

work/ (89 notes)
  Good subfolder usage ✅
```

## Common Workflows

### Monthly Vault Maintenance

```bash
# 1. Overall health check
/vault-health

# 2. Find and fix issues
/vault-orphans        # Link or archive
/vault-fix-links      # Repair broken links
/vault-gaps           # Create missing notes

# 3. Optimize organization
/vault-folder-health  # Review structure
/vault-clusters       # Identify topic areas
```

### Research Session

```bash
# Starting research on a topic
/vault-search --tags research
/vault-related "Topic Name"
/vault-gaps  # What's missing?

# Find background material
/vault-backlinks "Core Concept"
/vault-hubs      # Find central reference notes
```

### Content Audit

```bash
# Find neglected but important notes
/vault-stale

# Find isolated content
/vault-orphans
/vault-dead-ends

# Check link quality
/vault-fix-links
/vault-unlinked-mentions "Key Term"
```

## Best Practices

### 1. Regular Health Checks

Run `/vault-health` weekly or monthly to track:
- Orphan rate trends
- Link density growth
- Knowledge gap evolution

### 2. Progressive Cleanup

Don't try to fix everything at once:
- Week 1: Fix broken links
- Week 2: Address orphans
- Week 3: Fill knowledge gaps
- Week 4: Optimize folder structure

### 3. Follow the Connections

Use backlinks and related notes to:
- Discover unexpected connections
- Find notes you forgot about
- Identify emerging themes

## Troubleshooting

### "MCP server not found"

**Install smoking-mirror:**
- [WSL Setup](../installation/wsl.md)
- [Windows Setup](../installation/windows.md)
- [MCP Servers Guide](../installation/mcp-servers.md)

### Skills show "requires smoking-mirror"

Restart Claude Code after configuring MCP server:
```bash
# Exit and restart in vault
cd /path/to/vault
claude
```

### Slow [[Performance]]

Large vaults (5000+ [[Notes]]) may be slow:
- [[Use]] more [[Specific]] searches (folders, [[Tags]])
- [[Run]] analyses during off-[[Hours]]
- [[Consider]] vault archiving [[Strategies]]

## Related Features

- **[Wikilinks](wikilinks.md)** - [[Auto]]-[[Linking]] supports vault health
- **[Examples: Vault Analysis](../examples/vault-analysis.md)** - Step-by-step [[Workflows]]

---

*"Your vault is a living garden, dear scholar. Let the owl help [[You]] tend it with wisdom!"* 🦉🧠
