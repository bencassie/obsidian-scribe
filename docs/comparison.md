# Comparison

How Obsidian Scribe compares to other AI tools for Obsidian.

---

## Feature Matrix

| Feature | Obsidian Scribe | Copilot | Smart Connections |
|---------|-----------------|---------|-------------------|
| **Vault Analysis** | ✅ 15 skills | ❌ | ❌ |
| **Achievement Tracking** | ✅ 126 patterns | ❌ | ❌ |
| **Hierarchical Rollups** | ✅ 5 agents | ❌ | ❌ |
| **Wikilink Automation** | ✅ Auto-apply | ❌ | ❌ |
| **Works from Terminal** | ✅ Claude Code | ❌ | ❌ |
| **Semantic Search** | Via MCP | ✅ | ✅ |
| **Chat with Notes** | ✅ | ✅ | ✅ |
| **Long Context (200K)** | ✅ Claude | Limited | ❌ |
| **Local-First** | ✅ | ✅ | ✅ |
| **Price** | Free (MIT) | Free + Pro | Free + Pro |

---

## Obsidian Scribe

**Best for:** Power users who want to drive their vault from the command line.

### Strengths
- Full vault intelligence (orphans, hubs, clusters, gaps)
- Automatic achievement detection from daily logs
- Multi-agent summarization (daily → yearly)
- Works entirely from Claude Code terminal
- Cross-platform (WSL + Windows)
- Free and open source

### Limitations
- Requires Claude Code (not in-Obsidian)
- Some features need smoking-mirror MCP
- No semantic embeddings (graph-based, not AI similarity)

---

## Copilot for Obsidian

**Best for:** Chat-based Q&A about your notes.

### Strengths
- Simple chat interface inside Obsidian
- Good for asking questions about content
- Works with local LLMs

### Limitations
- No vault analysis (can't find orphans, gaps, etc.)
- No achievement tracking
- No hierarchical summarization
- Chat only—no automation

---

## Smart Connections

**Best for:** Finding semantically similar notes.

### Strengths
- Semantic embeddings for similarity search
- "Related notes" suggestions
- Works offline with local models

### Limitations
- Similarity only—no structural analysis
- No achievement tracking
- No rollup summarization
- In-Obsidian only

---

## When to Use Each

### Use Obsidian Scribe when you want to:
- Analyze your vault structure (orphans, hubs, link density)
- Auto-track achievements for performance reviews
- Generate weekly/monthly/quarterly summaries
- Work from the terminal
- Automate wikilink suggestions

### Use Copilot when you want to:
- Ask questions about note content
- Have a conversation inside Obsidian
- Use local LLMs

### Use Smart Connections when you want to:
- Find semantically similar notes
- Get "related content" suggestions
- Work offline

---

## Why Claude Code?

Obsidian Scribe is built on Claude Code because:

1. **200K context window** — Analyze your entire vault at once
2. **Skills & hooks** — Automate without plugins
3. **Multi-agent orchestration** — Coordinate complex summaries
4. **Terminal-first** — No GUI switching
5. **Cross-platform** — Same experience on WSL + Windows

---

## Combining Tools

You can use Obsidian Scribe alongside other tools:

- **Scribe for structure** — Vault analysis, rollups, achievements
- **Copilot for chat** — Q&A inside Obsidian
- **Smart Connections for similarity** — Find related notes

They don't conflict—each handles different use cases.

---

## Related

- [Quick Start](getting-started.md) — Get running in 5 minutes
- [Skills Reference](skills-reference.md) — All 21 skills
