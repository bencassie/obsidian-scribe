# Comparison

How Obsidian Scribe compares to other AI tools for Obsidian.

---

## Why Not RAG?

[RAG](https://en.wikipedia.org/wiki/Retrieval-Augmented_Generation) (Retrieval-Augmented Generation) is the standard approach for AI + knowledge bases. But for [PKM](https://en.wikipedia.org/wiki/Personal_knowledge_management), it has fundamental limitations:

| RAG Approach | Graph-First Approach |
|--------------|---------------------|
| Embed chunks → retrieve similar | Query relationships → understand structure |
| "Here are 10 similar paragraphs" | "Here's how these 3 notes connect to 12 others" |
| Static retrieval | Interactive REPL loop |
| Read-only | Read, write, and automate |
| No understanding of links | Full backlink/forward link awareness |
| Chunks lose context | Graph preserves relationships |

**The Claude Code REPL loop changes everything.** It's not retrieval—it's a conversation with your knowledge graph. Ask a question, get an answer, ask a follow-up, take action, all in one session.

---

## The Problem with File-Centric AI

Traditional AI tools (including RAG) read your vault file-by-file:

- 50 files × 1000 tokens = 50K tokens consumed
- Shallow understanding—no relationships
- Can't see the graph structure
- Can't take action on what it finds

**Obsidian Scribe + smoking-mirror is different.** It treats your vault as a **queryable knowledge graph**.

---

## Graph-First Navigation

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

> **smoking-mirror gives Claude the map, not the territory.**

---

## The REPL Advantage

RAG is one-shot: embed → retrieve → answer → done.

Claude Code is a **conversation**:

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

## Feature Matrix

| Feature | Obsidian Scribe | Copilot | Smart Connections |
|---------|-----------------|---------|-------------------|
| **Vault Analysis** | 28 skills | - | - |
| **Achievement Tracking** | 126 patterns | - | - |
| **Hierarchical Rollups** | 5 agents | - | - |
| **Wikilink Automation** | Auto-apply | - | - |
| **Works from Terminal** | Claude Code | - | - |
| **Semantic Search** | Via MCP | Yes | Yes |
| **Chat with Notes** | Yes | Yes | Yes |
| **Long Context (200K)** | Claude | Limited | - |
| **Local-First** | Yes | Yes | Yes |
| **Price** | Free (MIT) | Free + Pro | Free + Pro |

---

## Detailed Comparison

| Feature | Obsidian Scribe + smoking-mirror | RAG Solutions | Copilot | Smart Connections |
|---------|----------------------------------|---------------|---------|-------------------|
| **Graph tools** | 47 specialized tools | None | - | - |
| **Privacy** | Content stays local | Embeddings sent | Varies | Varies |
| **Token efficiency** | 200x savings | Embed everything | - | - |
| **Interactive REPL** | Conversation loop | One-shot | - | - |
| **Take action** | Read + Write + Automate | Read-only | Chat only | - |
| **Backlink awareness** | Native | Lost in chunking | - | - |
| **Frontmatter queries** | Full schema analysis | - | - | - |
| **Section extraction** | Without reading whole file | - | - | - |
| **Link path finding** | A → B → C routes | - | - | - |
| **Task management** | Cross-vault tasks | - | - | - |
| **Orphan/hub detection** | Automated | - | - | - |
| **Vault health analysis** | 28 skills | - | - | - |
| **Achievement tracking** | 126 patterns | - | - | - |
| **Intelligent agents** | 8 agents (rollups, schema, relationships) | - | - | - |
| **Follow-up questions** | Full context preserved | Re-retrieve each time | Yes | - |
| **Long context (200K)** | Claude | Varies | Limited | - |
| **Price** | Free (MIT) | Varies | Free + Pro | Free + Pro |

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
- [Skills Reference](skills-reference.md) — All 28 skills
