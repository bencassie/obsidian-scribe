<div align="center">

<img src="docs/assets/logo-alt.png" alt="Obsidian Scribe" width="200">

# Obsidian Scribe

**Your entire Obsidian vault, accessible from the command line.**

21 skills • 4 smart hooks • 5 rollup agents • Full vault intelligence

[![License: MIT](https://img.shields.io/badge/License-MIT-gold.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-8B5CF6)](https://github.com/anthropics/claude-code)

</div>

---

<img src="docs/assets/banner.png" alt="Obsidian Scribe in action" width="100%">

## Why This Exists

Obsidian is powerful. But maintaining a vault at scale is *work*:
- Manually linking notes gets tedious at 1000+ notes
- Finding orphans, broken links, knowledge gaps = clicking around
- Summarizing weekly/monthly progress = copy-paste hell
- Tracking achievements for reviews = hoping you remember

**Obsidian Scribe brings your vault into Claude Code.** Query it. Analyze it. Automate it. All from your terminal.

---

## What You Get

| Category | Commands | What It Does |
|----------|----------|--------------|
| **Daily Capture** | `/auto-log`, `/task-add` | Timestamped logging, task creation with natural dates |
| **Vault Analysis** | 15 `/vault-*` commands | Orphans, hubs, clusters, gaps, broken links, stale notes |
| **Wikilink Automation** | `/wikilink-apply`, hooks | Auto-suggest links, syntax validation, cache management |
| **Periodic Rollups** | `/rollup` + 5 agents | Daily → Weekly → Monthly → Quarterly → Yearly summaries |
| **Achievement Tracking** | Auto-detect hook | 126 patterns to capture wins from logs |

**Total: 21 skills, 4 hooks, 5 specialized agents**

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

You: /vault-orphans

Scribe: Found 43 orphan notes. Top candidates for linking:
        - projects/old-mvp-notes.md (created 6mo ago)
        - research/llm-fine-tuning.md (has valuable content)
        ...

You: /auto-log Fixed the authentication bug, deployed v2.1

Scribe: ✓ Added to daily note (14:32)
        🏆 Achievement detected: "Fixed authentication bug"
        → Added to Achievements.md
```

No clicking. No switching apps. Your vault responds to conversation.

---

## Quick Start

### Install

```bash
/install bencassie/obsidian-scribe
```

### Try It

```bash
cd /path/to/your/vault
claude

# Check vault health
/vault-health

# Log something
/auto-log Started working on new feature

# Run a weekly rollup
/rollup-weekly 2026-W01
```

---

## Graph-First Workflow

Obsidian Scribe works best with the **graph-first** mental model. Instead of treating your vault as files to search, treat it as a knowledge graph to navigate.

### The Three-Layer Architecture

```
Layer 1: INTELLIGENCE (smoking-mirror MCP)
  - Your eyes: Navigate, discover, understand relationships
  - Query backlinks, hubs, orphans, clusters
  - Search by tags, frontmatter, semantic meaning

Layer 2: WORKFLOWS (obsidian-scribe skills)
  - Your brain: Execute patterns, maintain health
  - Daily logging, rollups, vault maintenance

Layer 3: CONTENT (Read/Edit/Write)
  - Your hands: Only touch what navigation identified
  - Surgical reads after graph queries
```

### The Key Insight

> **smoking-mirror gives Claude the map, not the territory.**

**Old way (file-centric)**: Grep → Read 50 files → 50K tokens → shallow understanding

**New way (graph-first)**: Query graph → Read 3 key files → 5K tokens → deep understanding

See [WORKFLOW.md](WORKFLOW.md) for the complete guide, or copy [CLAUDE.md.example](CLAUDE.md.example) to your vault.

---

## All Skills

### Core Workflows (5 skills)

| Skill | Description |
|-------|-------------|
| `/auto-log <text>` | Add timestamped entry to today's daily note |
| `/task-add <text>` | Create task with natural language due date |
| `/rollup` | Execute full rollup chain (last 2 months) |
| `/rebuild-wikilink-cache` | Rebuild entity cache from vault |
| `/wikilink-apply <file>` | Apply wikilink suggestions to a note |

### Vault Health (16 skills) — requires [smoking-mirror MCP](docs/installation/mcp-servers.md)

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

### Periodic Rollups (4 additional skills)

| Skill | Description |
|-------|-------------|
| `/rollup-weekly <week>` | Summarize week (e.g., `2026-W01`) |
| `/rollup-monthly <month>` | Summarize month (e.g., `2026-01`) |
| `/rollup-quarterly <quarter>` | Summarize quarter (e.g., `2026-Q1`) |
| `/rollup-yearly <year>` | Summarize year (e.g., `2026`) |

---

## Smart Hooks

These run automatically on every edit:

| Hook | Trigger | What It Does |
|------|---------|--------------|
| `session-start` | Session start | Shows vault status, recent achievements |
| `achievement-detect` | After edits | Detects wins from logs (126 patterns) |
| `wikilink-suggest` | After edits | Auto-applies wikilinks to known entities |
| `syntax-validate` | After edits | Warns about syntax issues |

---

## Achievement Detection

The achievement hook watches for patterns like:
- **Actions**: Built, created, deployed, fixed, shipped
- **Progress**: Completed, finished, launched
- **Success signals**: Works, passed, all tests green
- **Milestones**: v1.0, first time, breakthrough
- **Bold text**: `**Anything in bold**` = important
- **Emojis**: ✅ 🎉 🚀 💪 🏆

When detected, achievements auto-add to your `Achievements.md` for performance reviews.

---

## Dependencies

### Required
- **Python 3.8+** — Hooks are written in Python

### Optional (for vault intelligence)
- **[smoking-mirror MCP](docs/installation/mcp-servers.md)** — Enables 15 vault analysis skills

---

## Cross-Platform Setup

This plugin works on both WSL and Windows using dual-config architecture.

### WSL (Committed to Git)

Configure in `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "obsidian-scribe": {
      "source": {
        "source": "github",
        "repo": "bencassie/obsidian-scribe"
      }
    }
  }
}
```

### Windows (Local Override)

Configure in `C:\Users\<you>\.claude.json`:

```json
{
  "projects": {
    "C:/Users/<you>/obsidian/<vault>": {
      "extraKnownMarketplaces": {
        "obsidian-scribe": {
          "source": {
            "source": "github",
            "repo": "bencassie/obsidian-scribe"
          }
        }
      }
    }
  }
}
```

**Note**: Use forward slashes `/` in all paths on Windows.

See [Windows Setup](docs/installation/windows.md) | [WSL Setup](docs/installation/wsl.md) for detailed instructions.

---

## Comparison

| Feature | Obsidian Scribe | Copilot | Smart Connections |
|---------|-----------------|---------|-------------------|
| Full vault analysis | ✅ 15 skills | ❌ Chat only | ❌ Semantic only |
| Achievement tracking | ✅ 126 patterns | ❌ | ❌ |
| Hierarchical rollups | ✅ 5 agents | ❌ | ❌ |
| Works from terminal | ✅ Claude Code | ❌ In-Obsidian | ❌ In-Obsidian |
| Long context (200K) | ✅ Claude | Limited | ❌ |
| Local-first | ✅ | ✅ | ✅ |
| Price | Free (MIT) | Free + Pro | Free + Pro |

---

## Documentation

- **[Quick Start](docs/getting-started.md)** — Get running in 5 minutes
- **[Skills Reference](docs/skills-reference.md)** — All 21 skills documented
- **[Workflows](docs/workflows.md)** — Real examples and use cases
- **[Comparison](docs/comparison.md)** — vs other tools
- **Setup**: [Windows](docs/installation/windows.md) | [WSL](docs/installation/wsl.md) | [MCP Servers](docs/installation/mcp-servers.md)

---

## License

MIT
