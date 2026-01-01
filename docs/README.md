# Documentation

Obsidian Scribe — Your Obsidian vault, accessible from the command line.

---

## Quick Links

| Topic | Description |
|-------|-------------|
| [Getting Started](getting-started.md) | Get running in 5 minutes |
| [Skills Reference](skills-reference.md) | All 21 skills documented |
| [Workflows](workflows.md) | Real examples and use cases |
| [Comparison](comparison.md) | vs Copilot, Smart Connections |

---

## Installation

| Platform | Guide |
|----------|-------|
| Windows | [Windows Setup](installation/windows.md) |
| WSL/Linux | [WSL Setup](installation/wsl.md) |
| MCP (vault intelligence) | [MCP Servers](installation/mcp-servers.md) |

---

## Features

### Daily Capture
- `/auto-log` — Timestamped logging
- `/task-add` — Task creation with natural dates
- `/food` — Food tracking

### Vault Intelligence (15 skills)
- `/vault-health` — Comprehensive diagnostics
- `/vault-orphans` — Find isolated notes
- `/vault-gaps` — Find undocumented topics
- [Full list →](skills-reference.md#vault-intelligence)

### Wikilink Automation
- `/rebuild-wikilink-cache` — Rebuild entity cache
- `/wikilink-apply` — Apply links to a note
- Auto-suggest hook

### Periodic Rollups
- `/rollup` — Full chain (daily → yearly)
- `/rollup-weekly`, `/rollup-monthly`, etc.
- 5 specialized agents

### Achievement Tracking
- 126 pattern detection
- Auto-add to Achievements.md
- Works with daily logs

---

## Architecture

```
21 skills + 4 hooks + 5 agents
         ↓
    Claude Code
         ↓
   Your Obsidian Vault
```

**Dependencies:**
- Python 3.8+ (for hooks)
- smoking-mirror MCP (for vault-* skills)

---

## Support

- [Report Issues](https://github.com/bencassie/obsidian-scribe/issues)
- [Feature Requests](https://github.com/bencassie/obsidian-scribe/discussions)
