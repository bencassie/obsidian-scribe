# Obsidian-Scribe Graph-First Workflow Guide

**For users who want to revolutionize their Obsidian PKM workflow with Claude Code**

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [The Graph-First Mental Model](#the-graph-first-mental-model)
3. [Quick Start](#quick-start)
4. [Configuration Guide](#configuration-guide)
5. [Core Workflow Patterns](#core-workflow-patterns)
6. [Tool Reference](#tool-reference)
7. [Migration Guide](#migration-guide)
8. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before adopting this workflow, you need:

- [ ] **Claude Code CLI** installed ([Installation Guide](https://claude.ai/code))
- [ ] **smoking-mirror MCP** server configured (see [Configuration Guide](#configuration-guide))
- [ ] **obsidian-scribe plugin** installed from GitHub

### Quick Setup

```bash
# Install obsidian-scribe plugin
/install bencassie/obsidian-scribe

# Verify installation
/skills
# Should show: 21 skills from obsidian-scribe
```

---

## The Graph-First Mental Model

### The Paradigm Shift

Traditional Obsidian PKM workflows treat your vault as a **file collection**. The graph-first approach treats it as a **knowledge graph**.

**OLD WAY (File-Centric)**:
```
You: "Claude, find notes about my Python projects"
Claude: *uses grep to search file contents*
        *reads 30+ files*
        *50K+ tokens consumed*
        *shallow understanding (no relationships)*
```

**NEW WAY (Graph-First)**:
```
You: "Claude, find notes about my Python projects"
Claude: *queries smoking-mirror graph*
        search_notes(has_tag="python", has_tag="project")
        get_backlinks() to understand connections
        *reads only 3-5 core notes*
        *5K tokens consumed*
        *deep understanding (relationships, context, clusters)*
```

### The Core Insight

> **smoking-mirror gives Claude the map, not the territory.**

Your vault becomes a **queryable knowledge graph** where Claude can:
- Navigate by relationships (backlinks, forward links, clusters)
- Search by meaning (tags, frontmatter, semantic queries)
- Understand structure (hubs, orphans, dead-ends)
- Extract content surgically (sections, tasks, metadata)

**Without reading every file.**

### Three-Layer Architecture

```
Layer 1: INTELLIGENCE (smoking-mirror MCP)
  - Vault structure understanding
  - Link graph traversal (backlinks, hubs, clusters)
  - Semantic search (tags, frontmatter, titles)
  - Entity discovery (all linkable things)
  - Relationship analysis

Layer 2: WORKFLOWS (obsidian-scribe skills)
  - User workflows (auto-log, rollup, task-add)
  - Vault maintenance (health, orphans, fix-links)
  - Summarization (weekly/monthly/quarterly agents)

Layer 3: CONTENT OPERATIONS (Read/Edit/Write)
  - Reading specific note content
  - Editing identified sections
  - Writing new notes
  - Only AFTER navigation identifies targets
```

**The Mental Model**:
- **smoking-mirror = Your eyes** (navigate, discover, understand)
- **obsidian-scribe = Your brain** (execute workflows, automate patterns)
- **File tools = Your hands** (read, edit, write content)

---

## Quick Start

### Step 1: Configure smoking-mirror MCP

Create or edit your `.mcp.json` file in your vault root:

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
        "OBSIDIAN_VAULT_PATH": "C:/absolute/path/to/your/vault"
      }
    }
  }
}
```

### Step 2: Enable obsidian-scribe Plugin

Create or edit `.claude/settings.local.json` in your vault root:

```json
{
  "permissions": {
    "allow": [
      "mcp__smoking-mirror__*",
      "Skill(obsidian-scribe:*)"
    ]
  },
  "enabledPlugins": {
    "obsidian-scribe@obsidian-scribe": true
  }
}
```

### Step 3: Create Your CLAUDE.md

Create a `CLAUDE.md` file in your vault root with graph-first instructions.

**Minimal template**:

```markdown
# My Obsidian Vault - Claude Code Instructions

## Core Philosophy: Graph-First Navigation

Use **smoking-mirror MCP** as the primary navigation layer.

### Tool Hierarchy
1. **smoking-mirror** - Discovery & navigation
2. **obsidian-scribe skills** - Workflows
3. **Read/Edit/Write** - Content operations (only after navigation)

### Navigation Principles
- Use `search_notes()` instead of Grep
- Use `get_backlinks()` to understand relationships
- Use `find_orphan_notes()` for disconnected content
- Use `get_section_content()` instead of reading full files

## smoking-mirror Quick Reference

| Tool | Purpose |
|------|---------|
| `search_notes()` | Find notes by tags, frontmatter, title |
| `get_backlinks(path)` | Who links TO this note |
| `get_forward_links(path)` | What this note links TO |
| `find_orphan_notes()` | Disconnected notes |
| `find_hub_notes()` | Highly connected notes |
| `get_all_tasks()` | All tasks in vault |
| `get_section_content(path, heading)` | Extract specific section |
```

**Full template**: See the [example CLAUDE.md](https://github.com/bencassie/obsidian-scribe/blob/main/CLAUDE.md.example) in the obsidian-scribe repo.

### Step 4: Verify Setup

```bash
# Start Claude Code in your vault
claude

# Check that smoking-mirror connected
# Look for: "MCP server 'smoking-mirror': Successfully connected"

# Check that obsidian-scribe loaded
# Look for: "Found X plugins (X enabled, 0 disabled)"

# Test a query
/vault-health
```

---

## Configuration Guide

### Required Files

| File | Location | Purpose | Git Status |
|------|----------|---------|------------|
| `.mcp.json` | Vault root | smoking-mirror MCP config | Committed |
| `.claude/settings.local.json` | Vault root | Plugin permissions | Gitignored |
| `CLAUDE.md` | Vault root | Claude instructions | Committed |

### Optional Files

| File | Location | Purpose | Git Status |
|------|----------|---------|------------|
| `.claude/settings.json` | Vault root | Project-wide settings | Committed |
| `.claude/rules/*.md` | Vault root | Path-scoped rules | Committed |

### Permissions Setup

**Minimal permissions** (in `.claude/settings.local.json`):

```json
{
  "permissions": {
    "allow": [
      "Read(**/*.md)",
      "Edit(**/*.md)",
      "Write(**/*.md)",
      "mcp__smoking-mirror__*",
      "Skill(obsidian-scribe:*)"
    ],
    "deny": [
      "Read(.obsidian/**)",
      "Edit(.git/**)"
    ]
  },
  "enabledPlugins": {
    "obsidian-scribe@obsidian-scribe": true
  }
}
```

### Cross-Platform Configuration

**WSL Users**: Use Unix paths in `.mcp.json`:
```json
"env": {
  "OBSIDIAN_VAULT_PATH": "/mnt/c/Users/username/Documents/vault"
}
```

**Windows Users**: Use Windows paths + `cmd` wrapper:
```json
"command": "cmd",
"args": ["/c", "npx", "-y", "smoking-mirror@latest"],
"env": {
  "OBSIDIAN_VAULT_PATH": "C:/Users/username/Documents/vault"
}
```

---

## Core Workflow Patterns

### Daily Operations

**Morning workflow**:

```
1. Start Claude Code session
   → Vault intelligence displayed (session-start hook)
   → Daily note status, orphan count, broken links, stale hubs

2. Check what needs attention:
   "What important notes haven't I touched this week?"
   → Claude uses: get_stale_notes(days=7, min_backlinks=2)

3. Review recent work:
   "What have I worked on the last 3 days?"
   → Claude uses: get_recent_notes(days=3)

4. Check tasks:
   "What tasks are due today?"
   → Claude uses: get_tasks_with_due_dates()

5. Log work:
   "Log: Finished Python project refactoring"
   → Claude uses: /auto-log skill
```

### Weekly Maintenance

Run these skills regularly:

```bash
# Vault health overview
/vault-health

# Find disconnected notes
/vault-orphans

# Find broken links
/vault-fix-links

# Check important but neglected notes
/vault-stale
```

### Monthly Deep Maintenance

```bash
# Generate weekly/monthly summaries
/rollup

# Review vault structure
/vault-hubs         # What are my key concepts?
/vault-clusters     # What groups of related notes exist?
/vault-gaps         # What topics am I missing?
```

### Finding Context

**Example task**: "Understand everything about my Claude Code notes"

**Graph-first approach**:

```
You: "Find all notes about Claude Code and show me how they're connected"

Claude:
1. search_notes(title_contains="Claude Code")
   → 3 notes directly about it

2. get_backlinks("tech/tools/Claude Code.md")
   → 12 notes that reference it

3. find_hub_notes()
   → Check if Claude Code is a hub (highly connected)

4. get_unlinked_mentions("Claude Code")
   → 8 places mentioned but not linked

5. Surgically read only the 3 core notes

Result: Deep understanding with minimal token usage
```

### Vault Maintenance

**Example task**: "Clean up my vault"

**Graph-first approach**:

```
You: "What needs cleaning up in my vault?"

Claude:
1. find_orphan_notes()
   → 23 disconnected notes

2. find_broken_links()
   → 4 invalid wikilinks with fix suggestions

3. find_dead_ends(min_backlinks=2)
   → Notes that should link out but don't

4. For each issue, use:
   - /vault-fix-links (automated repair)
   - /vault-suggest (linking opportunities)
   - Selective reads only as needed
```

---

## Tool Reference

### smoking-mirror MCP Tools

Full documentation: [smoking-mirror README](https://github.com/bencassie/smoking-mirror)

**Most Common Tools**:

| Tool | Use Case | Example |
|------|----------|---------|
| `search_notes()` | Find notes by metadata | `search_notes(has_tag="project", folder="work")` |
| `get_backlinks(path)` | Who links to this note | `get_backlinks("tech/Python.md")` |
| `get_forward_links(path)` | What this note links to | `get_forward_links("projects/Main.md")` |
| `find_orphan_notes()` | Disconnected notes | `find_orphan_notes()` |
| `find_hub_notes(min)` | Highly connected notes | `find_hub_notes(min_links=5)` |
| `get_all_tasks()` | All tasks in vault | `get_all_tasks(status="open")` |
| `get_section_content(path, heading)` | Extract section | `get_section_content("note.md", "## Ideas")` |
| `get_unlinked_mentions(entity)` | Where X mentioned but not linked | `get_unlinked_mentions("Python")` |

### obsidian-scribe Skills

**Core Workflows**:
- `/auto-log` - Log work to daily note
- `/task-add` - Add task with due date
- `/rollup` - Generate weekly/monthly summaries

**Vault Health**:
- `/vault-health` - Comprehensive health report
- `/vault-orphans` - Find disconnected notes
- `/vault-fix-links` - Repair broken links
- `/vault-suggest` - Suggest wikilinks (requires smoking-mirror)
- `/vault-stale` - Important but neglected notes
- `/vault-hubs` - Highly connected notes
- `/vault-clusters` - Groups of related notes

**Full skill list**: Run `/skills` to see all 21 skills

---

## Migration Guide

### From File-First to Graph-First

If you're used to traditional file-first Obsidian workflows, here's how to shift:

| Old Habit | New Approach | Why |
|-----------|--------------|-----|
| Grep for topics | `search_notes(title_contains="topic")` | Semantic search, no file reads |
| Manual backlink checking | `get_backlinks(path)` | Instant, comprehensive |
| Tree/ls for structure | `get_folder_structure()` | Structured, with note counts |
| Read files to find tasks | `get_all_tasks()` | All tasks, filtered, sorted |
| Manually check orphans | `find_orphan_notes()` | Automated detection |
| Manually trace connections | `get_link_path(from, to)` | Graph traversal |

### Sample Prompts (Graph-First)

**Instead of**:
```
"Claude, use grep to find all notes mentioning Python"
```

**Say**:
```
"Claude, find all notes about Python and show me how they connect"
```

**Instead of**:
```
"Claude, read through my weekly notes and summarize"
```

**Say**:
```
"Claude, what did I accomplish this month?" (uses /rollup)
```

**Instead of**:
```
"Claude, search for broken links in my vault"
```

**Say**:
```
"Claude, run /vault-health" (or /vault-fix-links for automated repair)
```

### Updating Your CLAUDE.md

Key sections to add for graph-first workflow:

1. **Core Philosophy** section (graph-first mental model)
2. **Tool Hierarchy** (smoking-mirror → skills → file ops)
3. **smoking-mirror Quick Reference** (most common tools)
4. **Tool Selection Guide** (DO/DON'T tables)
5. **Example Workflows** (showing graph-first approach)

See the [full CLAUDE.md example](https://github.com/bencassie/obsidian-scribe/blob/main/CLAUDE.md.example) for a complete template.

---

## Troubleshooting

### smoking-mirror Connection Issues

**Problem**: "MCP server 'smoking-mirror': Connection closed"

**Solution**:
- **Windows**: Ensure using `cmd /c npx` wrapper (not direct `npx`)
- **WSL**: Check that `npx` is in PATH
- **All platforms**: Verify `OBSIDIAN_VAULT_PATH` is absolute and correct

**Test**:
```bash
# Manually test smoking-mirror
npx -y smoking-mirror@latest
# (Windows: cmd /c npx -y smoking-mirror@latest)

# Should start and wait for JSON-RPC input
# Press Ctrl+C to exit
```

### Plugin Not Loading

**Problem**: Debug log shows "Found 0 plugins"

**Diagnosis**:
```bash
# Check plugin installation
/plugins

# Check debug log
cat ~/.claude/debug/<latest-session>.txt | grep "Found.*plugins"
```

**Solutions**:
- Ensure plugin installed: `/install bencassie/obsidian-scribe`
- Check `.claude/settings.local.json` has `enabledPlugins` entry
- Verify permissions allow `Skill(obsidian-scribe:*)`
- For local-scoped plugins, ensure working directory matches installation path

### Skills Not Working

**Problem**: `/vault-health` returns "smoking-mirror not available"

**Cause**: 16+ vault-* skills require smoking-mirror MCP connection

**Solution**:
1. Verify smoking-mirror connected (see above)
2. Check permissions allow `mcp__smoking-mirror__*`
3. Restart Claude Code session

### Hook Not Triggering

**Problem**: Wikilink suggestions not appearing after edits

**Diagnosis**:
```bash
# Check hooks loaded
cat ~/.claude/debug/<latest-session>.txt | grep "Registered.*hooks"
# Should show: "Registered 4 hooks from X plugins"
```

**Solutions**:
- Ensure plugin version matches across all 3 manifest files
- Run `/install bencassie/obsidian-scribe` to update
- Restart Claude Code session

### Common Error Messages

| Error | Meaning | Fix |
|-------|---------|-----|
| "Connection closed" (MCP) | Command failed to start | Check `cmd /c` wrapper on Windows |
| "Tool not found" | Permissions issue | Add tool to `.claude/settings.local.json` |
| "SSH authentication failed" | GitHub marketplace config wrong | Use `repo: "owner/repo"` format |
| "Found 0 plugins" | Plugin not loaded | Check installation, project path |

### Debug Log Locations

- **WSL**: `~/.claude/debug/<session-id>.txt`
- **Windows**: `C:\Users\<user>\.claude\debug\<session-id>.txt`

**Key indicators to check**:
- `Found X plugins (X enabled, 0 disabled)` - Plugins loaded
- `Registered X hooks from X plugins` - Hooks active
- `MCP server "smoking-mirror": Successfully connected` - MCP working
- `Total plugin skills loaded: X` - Skills available

---

## Resources

- **obsidian-scribe GitHub**: [github.com/bencassie/obsidian-scribe](https://github.com/bencassie/obsidian-scribe)
- **smoking-mirror GitHub**: [github.com/bencassie/smoking-mirror](https://github.com/bencassie/smoking-mirror)
- **Claude Code Docs**: [claude.ai/code](https://claude.ai/code)
- **Example CLAUDE.md**: [See repo](https://github.com/bencassie/obsidian-scribe/blob/main/CLAUDE.md.example)

---

## Contributing

Found issues or have suggestions for improving this workflow guide?

- **Issues**: [obsidian-scribe/issues](https://github.com/bencassie/obsidian-scribe/issues)
- **Discussions**: [obsidian-scribe/discussions](https://github.com/bencassie/obsidian-scribe/discussions)

---

**The key phrase to remember**:
> **smoking-mirror is your eyes, file tools are your hands.**
> Use your eyes to see where to go. Only use your hands when you know what to touch.

Welcome to graph-first Obsidian PKM. Your vault is now a queryable knowledge graph.
