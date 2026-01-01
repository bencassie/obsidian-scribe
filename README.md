<div align="center">

<img src="docs/assets/logo-alt.png" alt="Obsidian Scribe" width="200">

# Obsidian Scribe

**Talk to your Obsidian vault. From the command line.**

[![License: MIT](https://img.shields.io/badge/License-MIT-gold.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-8B5CF6)](https://github.com/anthropics/claude-code)
[![smoking-mirror](https://img.shields.io/badge/MCP-smoking--mirror-orange)](https://github.com/bencassie/smoking-mirror)

</div>

---

## The Problem

Your vault has grown. Finding things means clicking through folders, checking backlinks manually, remembering what you wrote six months ago. You're drowning in your own filing system.

## The Solution

Talk to your vault. It talks back—and takes action.

```
"Log that I shipped the feature"       → Timestamped in today's note. Achievement tracked.
"Summarize my week"                    → Weekly rollup created from daily notes.
"Add task: review PR by Friday"        → Task added with due date parsed.
"Find gaps in my documentation"        → 8 topics mentioned but never documented.
"Add wikilinks to this note"           → Plain text → [[linked concepts]].
```

Not just search. Write, automate, maintain.

---

## Quick Start

**Install the plugin:**

```
/plugin marketplace add bencassie/obsidian-scribe
/plugin install obsidian-scribe@bencassie/obsidian-scribe
```

**Try it:**

```
> How's my vault looking?

🔍 Vault Health Report
Notes: 2,847
Links: 8,234 (2.89 avg/note)
Orphans: 43 (1.5%)
Hubs: 12 highly-connected notes

⚠️ Knowledge gaps detected:
- "API authentication" mentioned 15x, no dedicated note
- "Database optimization" mentioned 9x, undocumented
```

---

## How It Works

```
You ──► obsidian-scribe ──► smoking-mirror ──► Your Vault
        (hands + voice)      (eyes)            (notes)
```

- **[obsidian-scribe](https://github.com/bencassie/obsidian-scribe)** — The Claude Code plugin. Takes your requests, executes workflows, writes to your vault.
- **[smoking-mirror](https://github.com/bencassie/smoking-mirror)** — The MCP server. Sees your vault's structure—backlinks, orphans, hubs, paths—without reading content.

> **smoking-mirror is your eyes, file tools are your hands.**
> Use your eyes to see where to go. Only use your hands when you know what to touch.

---

## What You Can Do

| Category | Count | Examples |
|----------|-------|----------|
| **Commands** (skills) | 28 | Vault health, daily logging, link analysis, rollups |
| **Automations** (hooks) | 5 | Achievement detection, wikilink suggestions, syntax validation |
| **Workflows** (agents) | 8 | Periodic summaries, schema enforcement, relationship exploration |

**[See all commands with examples →](docs/skills-reference.md)**

---

## Example Conversations

### Daily workflow

```
You: Log that I fixed the auth bug and deployed v2.1

Claude: ✓ Added to daily note (14:32)
        🏆 Achievement detected: "Fixed authentication bug"
        → Added to Achievements.md

You: Add task: write tests for the auth fix by Friday

Claude: ✓ Task added to daily note
        - [ ] Write tests for the auth fix 📅 2026-01-03
```

### End of week

```
You: Summarize my week

Claude: Creating weekly rollup from 5 daily notes...

        ✓ Created weekly-notes/2026-W01.md

        Highlights:
        - Shipped auth fix + v2.1 deployment
        - 3 achievements logged
        - 12 tasks completed, 2 carried forward
```

### Vault maintenance

```
You: Find notes that should be linked but aren't

Claude: Found 8 unlinked mentions of [[React]] across 5 notes.
        Found 4 unlinked mentions of [[authentication]] across 3 notes.

You: Add the wikilinks

Claude: ✓ Updated 8 files with [[React]] links
        ✓ Updated 3 files with [[authentication]] links
```

---

## Powered by smoking-mirror

The intelligence comes from **[smoking-mirror](https://github.com/bencassie/smoking-mirror)**, an MCP server that indexes your vault and exposes 47 graph query tools.

> **"tezcatl"** (Nahuatl) literally means "smoking mirror"—the original name for obsidian.
> The mirror reveals structure without taking content.

### What smoking-mirror sees

| Category | Tools | Purpose |
|----------|-------|---------|
| Graph Intelligence | 4 | Backlinks, forward links, orphans, hubs |
| Deep Graph Analysis | 6 | Link paths, common neighbors, bidirectional links |
| Wikilink Services | 4 | Suggestions, validation, broken link detection |
| Smart Search | 5 | Query by frontmatter, tags, dates, folders |
| Structure Analysis | 4 | Headings, sections, folder structure |
| Frontmatter Intelligence | 3 | Schema analysis, inconsistency detection |
| Task Management | 3 | Tasks across vault, due date filtering |
| Vault Health | 3 | Stats, activity patterns, folder structure |

**[Full smoking-mirror documentation →](https://github.com/bencassie/smoking-mirror)**

---

<img src="docs/assets/banner.png" alt="Obsidian Scribe in action" width="100%">

---

## Detailed Installation

### Step 1: Install the Plugin

In Claude Code:

```
/plugin marketplace add bencassie/obsidian-scribe
/plugin install obsidian-scribe@bencassie/obsidian-scribe
```

Or use the interactive UI: `/plugin` → Discover → obsidian-scribe → Install

### Step 2: Configure smoking-mirror MCP

Create `.mcp.json` in your vault root:

**WSL / macOS / Linux:**

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

**Windows (native):**

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

| Platform | Command | Path Format |
|----------|---------|-------------|
| WSL/Linux/macOS | `"command": "npx"` | `/mnt/c/...` or `/home/...` |
| Windows | `"command": "cmd"` with `"/c", "npx"` args | `C:/Users/...` (forward slashes) |

### Step 3: Verify

```bash
cd /path/to/your/vault
claude

> How's my vault looking?
```

**Detailed guides:** [Windows](docs/installation/windows.md) | [WSL](docs/installation/wsl.md) | [MCP](docs/installation/mcp-servers.md)

---

## Privacy by Design

**Your content never leaves your machine.**

```
    YOUR MACHINE                           │    CLOUD
    ────────────────────────────────────── │ ────────────────
                                           │
    ┌─────────────────┐                    │
    │   Obsidian      │                    │
    │     Vault       │  NEVER LEAVES      │
    │  ┌───────────┐  │  ───────────►      │   ❌ Blocked
    │  │ Notes     │  │                    │
    │  │ Journals  │  │                    │
    │  │ Private   │  │                    │
    │  └───────────┘  │                    │
    └────────┬────────┘                    │
             │                             │
             │ Parse locally               │
             ▼                             │
    ┌─────────────────┐                    │
    │  smoking-mirror │                    │
    │     (index)     │                    │
    └────────┬────────┘                    │
             │                             │
             │ Metadata only               │
             ▼                             │
    ┌─────────────────┐    API calls      ┌─────────────────┐
    │   Claude Code   │ ───────────────►  │    Claude AI    │
    └─────────────────┘  (paths, links,   └─────────────────┘
                          tags only)
```

**What Claude receives**: File paths, link relationships, tags, frontmatter keys, word counts, dates.

**What Claude NEVER receives**: Your actual note content—unless you explicitly `Read` it.

---

## Token Economy

Every character Claude reads costs tokens. smoking-mirror changes the math:

| Approach | Query | Tokens | Cost |
|----------|-------|--------|------|
| **Traditional** | "Read all notes with #project tag" | ~100,000 | ~$0.30 |
| **smoking-mirror** | `search_notes({ has_tag: "project" })` | ~500 | ~$0.0015 |

**200x savings per query.** Then Claude surgically reads only the 2-3 notes it actually needs.

---

## Performance

| Vault Size | Index Build | Query Time | Memory |
|------------|-------------|------------|--------|
| 100 notes | <200ms | <10ms | ~20MB |
| 500 notes | <500ms | <10ms | ~30MB |
| 1,500 notes | <2s | <10ms | ~50MB |
| 5,000 notes | <5s | <10ms | ~100MB |

Queries hit an in-memory index, not your filesystem. Instant results.

---

## Requirements

| Component | Required | Purpose |
|-----------|----------|---------|
| **[Claude Code](https://github.com/anthropics/claude-code)** | Yes | Runtime environment |
| **[smoking-mirror](https://github.com/bencassie/smoking-mirror) MCP** | Yes | Graph intelligence (vault-* commands depend on this) |
| **Python 3.8+** | Yes | Automations are written in Python |

---

## Documentation

- **[Skills Reference](docs/skills-reference.md)** — All 28 commands with natural language examples
- **[Use Cases](docs/use-cases.md)** — Real workflows with tool invocations
- **[Comparison](docs/comparison.md)** — How this compares to RAG, Copilot, Smart Connections
- **[WORKFLOW.md](WORKFLOW.md)** — Complete graph-first workflow guide
- **[CLAUDE.md.example](CLAUDE.md.example)** — Template for your vault's CLAUDE.md
- **[Example Rules](docs/example-rules/)** — Copy-paste rules for your `.claude/rules/` directory
- **Setup**: [Windows](docs/installation/windows.md) | [WSL](docs/installation/wsl.md) | [MCP Servers](docs/installation/mcp-servers.md)

---

## The Ecosystem

| Repository | Purpose |
|------------|---------|
| **[obsidian-scribe](https://github.com/bencassie/obsidian-scribe)** | Claude Code plugin: commands, automations, workflows |
| **[smoking-mirror](https://github.com/bencassie/smoking-mirror)** | MCP server: 47 graph tools for Obsidian |

Both are MIT licensed, free, and open source.

---

## License

MIT
