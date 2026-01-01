# Use Cases

Real-world examples showing how to use smoking-mirror and obsidian-scribe. Each use case shows what you say, what Claude does under the hood, and what you get back.

---

## For Daily Note Users

### Morning Activity Summary

**User Story**: As a daily note user, I want to see what I worked on recently, so I can plan today's work.

**You say:**
> "What did I work on this week?"
> "Show me recent activity"
> "What notes have I touched lately?"

**Claude uses:** `get_recent_notes(days=7)`

**You get:**

```json
{
  "count": 34,
  "days": 7,
  "notes": [
    {"path": "daily-notes/2026-01-01.md", "modified": "2026-01-01T16:05:31Z"},
    {"path": "projects/dashboard/api-design.md", "modified": "2026-01-01T14:22:18Z"},
    {"path": "tech/frameworks/React.md", "modified": "2025-12-31T11:45:00Z"},
    {"path": "weekly-notes/2026-W01.md", "modified": "2025-12-31T10:30:00Z"}
  ]
}
```

**Value**: Instantly see last week's activity without scrolling through folders. Great for standup meetings and weekly reviews.

---

### Task Deadline Tracking

**User Story**: As a daily note user, I want to see all tasks with due dates, so I don't miss deadlines.

**You say:**
> "What tasks are due soon?"
> "Show me upcoming deadlines"
> "What's overdue?"

**Claude uses:** `get_tasks_with_due_dates(status="open")`

**You get:**

```json
{
  "count": 8,
  "tasks": [
    {
      "task": "Review PR #123",
      "due": "2026-01-02",
      "source": "daily-notes/2026-01-01.md",
      "status": "open"
    },
    {
      "task": "Finish quarterly report",
      "due": "2026-01-15",
      "source": "projects/q1-planning.md",
      "status": "open"
    }
  ]
}
```

**Value**: Global view of deadlines across all notes, sorted by date. Never miss a deadline buried in an old note.

---

### Daily Capture

**User Story**: As a daily note user, I want to quickly log activities without leaving my workflow.

**You say:**
> "Log that I fixed the authentication bug"
> "Add to my daily: meeting with Sarah about roadmap"
> "Note: deployed v2.1 to production"

**Claude uses:** The `auto-log` skill, which:
1. Opens today's daily note (creates if missing)
2. Finds the `## Log` section
3. Appends timestamped entry

**Your daily note:**

```markdown
## Log
- 14:32 Fixed the authentication bug
- 15:15 Meeting with Sarah about roadmap
- 16:00 Deployed v2.1 to production
```

**Value**: Capture activities in real-time. The achievement hook automatically detects wins like "fixed", "deployed", "shipped" and logs them to your Achievements.md.

---

## For Knowledge Workers

### Discover Key Concepts

**User Story**: As a knowledge worker, I want to find my vault's most connected notes, so I can identify key concepts.

**You say:**
> "What are my hub notes?"
> "Find my most connected notes"
> "What are the central concepts in my vault?"

**Claude uses:** `find_hub_notes(min_links=5)`

**You get:**

```json
{
  "count": 12,
  "min_links": 5,
  "hubs": [
    {
      "path": "tech/frameworks/React.md",
      "backlinks": 47,
      "forward_links": 23,
      "total_connections": 70
    },
    {
      "path": "projects/Project Alpha.md",
      "backlinks": 32,
      "forward_links": 18,
      "total_connections": 50
    },
    {
      "path": "concepts/API Design.md",
      "backlinks": 28,
      "forward_links": 15,
      "total_connections": 43
    }
  ]
}
```

**Value**: Automatically discover which topics are central to your knowledge base. These are your MOCs (Maps of Content) whether you created them intentionally or not.

---

### Find Knowledge Gaps

**User Story**: As a knowledge worker, I want to find orphaned notes, so I can integrate disconnected knowledge.

**You say:**
> "Find orphan notes"
> "What notes aren't linked to anything?"
> "Show me knowledge islands"

**Claude uses:** `find_orphan_notes()`

**You get:**

```json
{
  "count": 43,
  "orphans": [
    "tech/tools/obscure-library.md",
    "projects/abandoned-idea.md",
    "personal/random-thought.md",
    "work/old-meeting-notes.md"
  ]
}
```

**Value**: Discover isolated notes that could be valuable if connected. These are linking opportunities - each orphan could enrich your knowledge graph.

---

### Understand Concept Relationships

**User Story**: As a knowledge worker, I want to see how two concepts connect, so I can understand their relationship.

**You say:**
> "How does React connect to Project Alpha?"
> "Find the path from API Design to Security"
> "What's the link chain between these notes?"

**Claude uses:** `get_link_path(from="tech/frameworks/React.md", to="projects/Project Alpha.md")`

**You get:**

```json
{
  "from": "tech/frameworks/React.md",
  "to": "projects/Project Alpha.md",
  "path": [
    "tech/frameworks/React.md",
    "tech/frontend/state-management.md",
    "projects/dashboard/frontend.md",
    "projects/Project Alpha.md"
  ],
  "distance": 3
}
```

**Value**: Trace the connection chain between any two notes. Understand how ideas relate through your actual linking patterns, not just proximity.

---

### Measure Connection Strength

**User Story**: As a knowledge worker, I want to measure how strongly two notes relate.

**You say:**
> "How related are React and Vue?"
> "Connection strength between API Design and Security"
> "Rate the relationship between these notes"

**Claude uses:** `get_connection_strength(note_a="tech/frameworks/React.md", note_b="tech/frameworks/Vue.md")`

**You get:**

```json
{
  "note_a": "tech/frameworks/React.md",
  "note_b": "tech/frameworks/Vue.md",
  "strength": 78,
  "factors": {
    "direct_link": true,
    "bidirectional": true,
    "shared_neighbors": 8,
    "common_tags": ["frontend", "javascript", "framework"],
    "path_distance": 1
  }
}
```

**Value**: Quantified relationship strength (0-100) with breakdown of contributing factors. Useful for understanding which concepts are truly related vs. just similar.

---

### Find Linking Opportunities

**User Story**: As a knowledge worker, I want to find mentions of a concept that aren't linked yet.

**You say:**
> "Find unlinked mentions of React"
> "Where is 'API design' mentioned but not linked?"
> "Show me linking opportunities for TypeScript"

**Claude uses:** `get_unlinked_mentions(entity="React")`

**You get:**

```json
{
  "entity": "React",
  "unlinked_count": 12,
  "mentions": [
    {
      "path": "daily-notes/2026-01-01.md",
      "context": "...working on React components for the dashboard..."
    },
    {
      "path": "projects/notes.md",
      "context": "...the React ecosystem has grown significantly..."
    },
    {
      "path": "tech/overview.md",
      "context": "...frameworks like React and Vue are popular..."
    }
  ]
}
```

**Value**: Discover plain text mentions that should be wikilinks. Each conversion strengthens your knowledge graph and improves discoverability.

---

## For Vault Maintainers

### Find Broken Links

**User Story**: As a vault maintainer, I want to find all broken wikilinks, so I can repair them.

**You say:**
> "Find broken links"
> "What wikilinks are dead?"
> "Show me link problems"

**Claude uses:** `find_broken_links()`

**You get:**

```json
{
  "broken_count": 23,
  "files_with_broken_links": 15,
  "broken_links": [
    {
      "source": "projects/dashboard.md",
      "link": "Old API Documentation",
      "suggestions": ["API Documentation", "API Reference"]
    },
    {
      "source": "tech/overview.md",
      "link": "Depracated Framework",
      "suggestions": ["Deprecated Framework"]
    }
  ]
}
```

**Value**: Automated link health monitoring across entire vault. Suggestions help you fix typos and renamed notes quickly.

---

### Schema Consistency Check

**User Story**: As a vault maintainer, I want to find frontmatter inconsistencies, so I can fix data quality issues.

**You say:**
> "Check my frontmatter for problems"
> "Find schema inconsistencies"
> "Audit my YAML fields"

**Claude uses:** `find_frontmatter_inconsistencies()`

**You get:**

```json
{
  "inconsistent_fields": {
    "tags": {
      "types": ["string", "array"],
      "count": 2,
      "examples": {
        "string": ["old-notes/meeting.md"],
        "array": ["projects/dashboard.md"]
      }
    },
    "priority": {
      "types": ["string", "number"],
      "count": 2,
      "examples": {
        "string": ["tasks/urgent.md"],
        "number": ["tasks/backlog.md"]
      }
    }
  },
  "total_inconsistencies": 2
}
```

**Value**: Detect fields with mixed types (string vs array, number vs string). Essential for Dataview queries and consistent metadata.

---

### Vault Health Overview

**User Story**: As a vault maintainer, I want comprehensive vault statistics, so I can understand overall health.

**You say:**
> "How's my vault looking?"
> "Give me vault health stats"
> "Vault overview"

**Claude uses:** `get_vault_stats()`

**You get:**

```json
{
  "notes": {
    "total": 2847,
    "with_frontmatter": 2341,
    "with_tags": 1892
  },
  "links": {
    "total_wikilinks": 8234,
    "avg_per_note": 2.89,
    "notes_with_backlinks": 2104,
    "orphan_notes": 43
  },
  "tags": {
    "unique_tags": 127,
    "total_usage": 4521,
    "top_tags": [
      {"tag": "project", "count": 342},
      {"tag": "work", "count": 289}
    ]
  },
  "structure": {
    "total_folders": 45,
    "avg_depth": 2.1,
    "largest_folder": "daily-notes (365 notes)"
  }
}
```

**Value**: Single query for note counts, link metrics, tag usage, folder distribution. Comprehensive health snapshot without reading any file content.

---

## The Token Economy

Every character Claude reads costs tokens. smoking-mirror changes the math:

**Before (file-centric approach):**

```
User: "Find notes about React"
Claude: grep("React") → 47 matches
        Read all 47 files → 50,000+ tokens
        Manual synthesis of relationships
```

**After (graph-first with smoking-mirror):**

```
User: "Find notes about React"
Claude: search_notes(title_contains="React") → 3 core notes
        get_backlinks("React.md") → 12 references
        get_unlinked_mentions("React") → 8 opportunities
        Surgically read 3 core notes → 5,000 tokens
```

**Result**: 90% token reduction, 10x faster, deeper understanding through relationships.

---

## Related

- [Skills Reference](skills-reference.md) - All 33 skills with natural language examples
- [smoking-mirror GitHub](https://github.com/bencassie/smoking-mirror) - Full MCP tool documentation
- [Workflows](workflows.md) - End-to-end workflow examples
