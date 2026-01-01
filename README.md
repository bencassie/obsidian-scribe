<div align="center">

<img src="docs/assets/logo-alt.png" alt="Obsidian Scribe" width="200">

# Obsidian Scribe

**Your [Obsidian](https://obsidian.md) vault as a queryable knowledge graph.**

[smoking-mirror](https://github.com/bencassie/smoking-mirror) MCP + 21 skills + 4 hooks + 5 agents = Graph-first PKM

[![License: MIT](https://img.shields.io/badge/License-MIT-gold.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-8B5CF6)](https://github.com/anthropics/claude-code)
[![smoking-mirror](https://img.shields.io/badge/MCP-smoking--mirror-orange)](https://github.com/bencassie/smoking-mirror)

</div>

---

## Who is this for?

| If you use... | You'll love this because... |
|---------------|----------------------------|
| **[Obsidian](https://obsidian.md)** | Finally query your vault's graph structure from the command line |
| **[Claude Code](https://github.com/anthropics/claude-code)** | Purpose-built plugin with 21 skills for knowledge management |
| **RAG systems** | Graph-first beats chunk-based retrieval for PKM (see below) |
| **[MCP](https://modelcontextprotocol.io/)** | [smoking-mirror](https://github.com/bencassie/smoking-mirror) is a production MCP server for Obsidian |

---

<img src="docs/assets/banner.png" alt="Obsidian Scribe in action" width="100%">

## Why Not RAG?

[RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) (Retrieval-Augmented Generation) is the standard approach for AI + knowledge bases. But for [PKM](https://en.wikipedia.org/wiki/Personal_knowledge_management), it has fundamental limitations:

| RAG Approach | Graph-First Approach |
|--------------|---------------------|
| Embed chunks → retrieve similar | Query relationships → understand structure |
| "Here are 10 similar paragraphs" | "Here's how these 3 notes connect to 12 others" |
| Static retrieval | Interactive REPL loop |
| Read-only | Read, write, and automate |
| No understanding of links | Full backlink/forward link awareness |
| Chunks lose context | Graph preserves relationships |

**The [Claude Code](https://github.com/anthropics/claude-code) REPL loop changes everything.** It's not retrieval—it's a conversation with your knowledge graph. Ask a question, get an answer, ask a follow-up, take action, all in one session.

---

## The Problem with File-Centric AI

Traditional AI tools (including RAG) read your vault file-by-file:
- 50 files × 1000 tokens = 50K tokens consumed
- Shallow understanding—no relationships
- Can't see the graph structure
- Can't take action on what it finds

**Obsidian Scribe + [smoking-mirror](https://github.com/bencassie/smoking-mirror) is different.** It treats your vault as a **queryable knowledge graph**.

---

## The Solution: Graph-First Navigation

Obsidian Scribe + [smoking-mirror MCP](https://github.com/bencassie/smoking-mirror) treats your vault as a **knowledge graph**, not a file system.

```
OLD WAY (file-centric):
  User: "Find notes about Project Alpha"
  Claude: Grep → 47 matches → Read all files → 50K+ tokens
          Manual synthesis, no relationships

NEW WAY (graph-first):
  User: "Find notes about Project Alpha"
  Claude: search_notes(title_contains="Project Alpha") → 3 core notes
          get_backlinks() → 12 notes that reference it
          get_unlinked_mentions() → 8 linking opportunities
          Surgically read 3 notes → 5K tokens
          Deep understanding with connections
```

> **[smoking-mirror](https://github.com/bencassie/smoking-mirror) gives Claude the map, not the territory.**

---

## The Three-Layer Architecture

```
YOUR EYES (smoking-mirror MCP)
  - Navigate: Where are things?
  - Discover: What exists?
  - Understand: How do things relate?
  ↓
YOUR BRAIN (obsidian-scribe skills)
  - Execute workflows
  - Maintain vault health
  - Automate patterns
  ↓
YOUR HANDS (Read/Edit/Write)
  - Read content
  - Edit text
  - Write files
```

**Use your eyes to see where to go. Only use your hands when you know what to touch.**

---

## What You Get

| Layer | Component | What It Provides |
|-------|-----------|------------------|
| **Intelligence** | [smoking-mirror](https://github.com/bencassie/smoking-mirror) MCP | 20+ graph queries: backlinks, hubs, orphans, clusters, tasks, sections |
| **Workflows** | 21 obsidian-scribe skills | Daily logging, vault health, rollups, wikilink automation |
| **Automation** | 4 smart hooks | Achievement detection, wikilink suggestions, syntax validation |
| **Summarization** | 5 rollup agents | Daily → Weekly → Monthly → Quarterly → Yearly summaries |

---

## How It Works

```
You: /vault-health

Scribe: 🔍 Vault Health Report
        Notes: 2,847
        Links: 8,234 (2.89 avg/note)
        Orphans: 43 (1.5%)
        Hubs: 12 highly-connected notes

        ⚠️ Knowledge gaps detected:
        - "API authentication" mentioned 15x, no dedicated note
        - "Database optimization" mentioned 9x, undocumented

You: Find all notes about Claude Code and how they connect

Scribe: [uses smoking-mirror graph queries]

        Core notes (3):
        - tech/tools/Claude Code.md (hub: 15 backlinks)
        - projects/claude-plugin.md
        - daily-notes/2026-01-01.md

        References (12 notes link to these)
        Unlinked mentions (8 opportunities to add [[wikilinks]])

        [reads only the 3 core notes for content]

You: /auto-log Fixed the authentication bug, deployed v2.1

Scribe: ✓ Added to daily note (14:32)
        🏆 Achievement detected: "Fixed authentication bug"
        → Added to Achievements.md
```

No clicking. No switching apps. Your vault responds to conversation.

---

## Quick Start

### 1. Install smoking-mirror MCP (Required)

Create `.mcp.json` in your vault root:

```json
{
  "mcpServers": {
    "smoking-mirror": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "smoking-mirror@latest"],
      "env": {
        "OBSIDIAN_VAULT_PATH": "/absolute/path/to/your/vault"
      }
    }
  }
}
```

**Windows users**: Use `cmd` wrapper:
```json
{
  "mcpServers": {
    "smoking-mirror": {
      "type": "stdio",
      "command": "cmd",
      "args": ["/c", "npx", "-y", "smoking-mirror@latest"],
      "env": {
        "OBSIDIAN_VAULT_PATH": "C:/Users/you/obsidian/vault"
      }
    }
  }
}
```

### 2. Install obsidian-scribe

```bash
/install bencassie/obsidian-scribe
```

### 3. Verify

```bash
cd /path/to/your/vault
claude

# Check vault health (uses smoking-mirror)
/vault-health

# Log something
/auto-log Started working on new feature
```

---

## smoking-mirror: Your Eyes

The power of this product comes from [**smoking-mirror MCP**](https://github.com/bencassie/smoking-mirror). It turns your vault into a queryable graph.

**GitHub**: [github.com/bencassie/smoking-mirror](https://github.com/bencassie/smoking-mirror)

### Graph Intelligence
| Tool | Purpose |
|------|---------|
| `get_backlinks(path)` | Who links TO this note |
| `get_forward_links(path)` | What this note links TO |
| `find_orphan_notes()` | Disconnected notes |
| `find_hub_notes(min=5)` | Central concepts |
| `get_link_path(from, to)` | Shortest path between notes |
| `find_bidirectional_links()` | Strong relationships (A ↔ B) |
| `find_dead_ends()` | Notes that should link out |

### Search & Discovery
| Tool | Purpose |
|------|---------|
| `search_notes()` | Dataview-like queries (tags, frontmatter, folders) |
| `get_recent_notes(days)` | Recently modified |
| `get_stale_notes(days)` | Important but neglected |
| `get_unlinked_mentions(entity)` | Linking opportunities |

### Structure Analysis
| Tool | Purpose |
|------|---------|
| `get_section_content(path, heading)` | Extract section without reading whole file |
| `get_note_metadata(path)` | Stats without content read |
| `get_all_tasks()` | Every task in vault |
| `get_folder_structure()` | Vault organization |

**Full tool reference**: [smoking-mirror GitHub](https://github.com/bencassie/smoking-mirror) — 20+ graph queries for Obsidian vaults

---

## obsidian-scribe: Your Brain

### Core Workflows (5 skills)

| Skill | Description |
|-------|-------------|
| `/auto-log <text>` | Add timestamped entry to today's daily note |
| `/task-add <text>` | Create task with natural language due date |
| `/rollup` | Execute full rollup chain (last 2 months) |
| `/rebuild-wikilink-cache` | Rebuild entity cache from vault |
| `/wikilink-apply <file>` | Apply wikilink suggestions to a note |

### Vault Health (16 skills)

| Skill | Description |
|-------|-------------|
| `/vault-health` | Comprehensive vault diagnostics |
| `/vault-stats` | Quick note/link/tag statistics |
| `/vault-orphans` | Find notes with no backlinks |
| `/vault-hubs` | Find highly-connected notes |
| `/vault-clusters` | Detect topic clusters |
| `/vault-gaps` | Find mentioned but undocumented topics |
| `/vault-stale` | Find important notes not updated recently |
| `/vault-dead-ends` | Notes with backlinks but no outlinks |
| `/vault-backlinks <note>` | Show all notes linking to a note |
| `/vault-related <note>` | Find similar notes |
| `/vault-fix-links` | Repair broken wikilinks |
| `/vault-unlinked-mentions <term>` | Find unlinked mentions of a term |
| `/vault-link-density` | Analyze link patterns |
| `/vault-folder-health` | Check folder organization |
| `/vault-search` | Advanced search with filters |
| `/vault-suggest` | Suggest wikilinks for a note |

### Periodic Rollups (4 skills + 5 agents)

| Skill | Description |
|-------|-------------|
| `/rollup-weekly <week>` | Summarize week (e.g., `2026-W01`) |
| `/rollup-monthly <month>` | Summarize month (e.g., `2026-01`) |
| `/rollup-quarterly <quarter>` | Summarize quarter (e.g., `2026-Q1`) |
| `/rollup-yearly <year>` | Summarize year (e.g., `2026`) |

---

## Smart Hooks

These run automatically:

| Hook | Trigger | What It Does |
|------|---------|--------------|
| `session-start` | Session start | Shows vault status, recent achievements |
| `achievement-detect` | After edits | Detects wins from logs (126 patterns) |
| `wikilink-suggest` | After edits | Auto-applies wikilinks to known entities |
| `syntax-validate` | After edits | Warns about syntax issues |

### Achievement Detection

The achievement hook watches for patterns like:
- **Actions**: Built, created, deployed, fixed, shipped
- **Progress**: Completed, finished, launched
- **Success signals**: Works, passed, all tests green
- **Milestones**: v1.0, first time, breakthrough
- **Bold text**: `**Anything in bold**` = important
- **Emojis**: ✅ 🎉 🚀 💪 🏆

When detected, achievements auto-add to your `Achievements.md` for performance reviews.

---

## Requirements

| Component | Required | Purpose |
|-----------|----------|---------|
| **[Claude Code](https://github.com/anthropics/claude-code)** | Yes | Runtime environment |
| **[smoking-mirror](https://github.com/bencassie/smoking-mirror) MCP** | Yes | Graph intelligence (16 vault-* skills depend on this) |
| **Python 3.8+** | Yes | Hooks are written in Python |

---

## Cross-Platform Setup

### WSL (Committed to Git)

`.mcp.json`:
```json
{
  "mcpServers": {
    "smoking-mirror": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "smoking-mirror@latest"],
      "env": {
        "OBSIDIAN_VAULT_PATH": "/mnt/c/Users/you/obsidian/vault"
      }
    }
  }
}
```

### Windows (Local Override)

In `C:\Users\<you>\.claude.json`:
```json
{
  "projects": {
    "C:/Users/<you>/obsidian/<vault>": {
      "mcpServers": {
        "smoking-mirror": {
          "type": "stdio",
          "command": "cmd",
          "args": ["/c", "npx", "-y", "smoking-mirror@latest"],
          "env": {
            "OBSIDIAN_VAULT_PATH": "C:/Users/<you>/obsidian/<vault>"
          }
        }
      }
    }
  }
}
```

**Note**: Use forward slashes `/` in all paths. Windows requires `cmd /c` wrapper for npx.

See [Windows Setup](docs/installation/windows.md) | [WSL Setup](docs/installation/wsl.md) for detailed instructions.

---

## Comparison

| Feature | Obsidian Scribe | RAG Solutions | Copilot | Smart Connections |
|---------|-----------------|---------------|---------|-------------------|
| **Graph navigation** | ✅ Full vault graph | ❌ Chunks only | ❌ | ❌ |
| **Interactive REPL** | ✅ Conversation loop | ❌ One-shot | ❌ | ❌ |
| **Take action** | ✅ Read + Write + Automate | ❌ Read-only | ❌ Chat only | ❌ |
| **Backlink awareness** | ✅ Native | ❌ Lost in chunking | ❌ | ❌ |
| **Orphan/hub detection** | ✅ Automated | ❌ | ❌ | ❌ |
| **Vault health analysis** | ✅ 16 skills | ❌ | ❌ | ❌ |
| **Achievement tracking** | ✅ 126 patterns | ❌ | ❌ | ❌ |
| **Hierarchical rollups** | ✅ 5 agents | ❌ | ❌ | ❌ |
| **Token efficiency** | ✅ 10x reduction | ⚠️ Embed everything | ❌ | ❌ |
| **Follow-up questions** | ✅ Full context preserved | ⚠️ Re-retrieve each time | ✅ | ❌ |
| **Semantic search** | ✅ Tags, frontmatter, graph | ✅ Embeddings | ✅ | ✅ Embeddings |
| **Long context (200K)** | ✅ Claude | Varies | Limited | ❌ |
| **Price** | Free (MIT) | Varies | Free + Pro | Free + Pro |

### The REPL Advantage

[RAG](https://en.wikipedia.org/wiki/Retrieval-augmented_generation) is one-shot: embed → retrieve → answer → done.

[Claude Code](https://github.com/anthropics/claude-code) is a **conversation**:
```
You: What do I know about authentication?
     [Claude queries graph, reads 3 notes]

You: How does that connect to the API project?
     [Claude follows links, finds 5 related notes]

You: Create a summary note linking these together
     [Claude writes new note with proper wikilinks]

You: Add it to my weekly rollup
     [Claude updates weekly note]
```

One session. Full context. Actions taken. That's the power of graph-first + REPL.

---

## Documentation

- **[WORKFLOW.md](WORKFLOW.md)** — Complete graph-first workflow guide
- **[CLAUDE.md.example](CLAUDE.md.example)** — Template for your vault's CLAUDE.md
- **[Example Rules](docs/example-rules/)** — Copy-paste rules for your `.claude/rules/` directory
- **[Skills Reference](docs/skills-reference.md)** — All 21 skills documented
- **[Workflows](docs/workflows.md)** — Real examples and use cases
- **Setup**: [Windows](docs/installation/windows.md) | [WSL](docs/installation/wsl.md) | [MCP Servers](docs/installation/mcp-servers.md)

### Example Rules

Ready-to-use [Claude Code rules](docs/example-rules/) for your vault:

| Rule | Purpose |
|------|---------|
| [achievements.md](docs/example-rules/achievements.md) | Achievement log format with timestamps |
| [daily-notes.md](docs/example-rules/daily-notes.md) | Daily note structure for rollup chain |
| [obsidian-syntax.md](docs/example-rules/obsidian-syntax.md) | Critical Obsidian markdown rules |
| [platform-requirements.md](docs/example-rules/platform-requirements.md) | WSL/Windows setup requirements |

Copy to `.claude/rules/` in your vault and customize paths.

---

## The Key Phrase

> **[smoking-mirror](https://github.com/bencassie/smoking-mirror) is your eyes, file tools are your hands.**
> Use your eyes to see where to go. Only use your hands when you know what to touch.

Welcome to graph-first [Obsidian](https://obsidian.md) PKM.

---

## The Ecosystem

| Repository | Purpose | Link |
|------------|---------|------|
| **obsidian-scribe** | Claude Code plugin: skills, hooks, agents | [GitHub](https://github.com/bencassie/obsidian-scribe) |
| **smoking-mirror** | MCP server: graph queries for Obsidian | [GitHub](https://github.com/bencassie/smoking-mirror) |

Both are MIT licensed, free, and open source. Star them if you find them useful.

---

## License

MIT
