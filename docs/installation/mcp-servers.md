# [[MCP]] [[Server]] Configuration 🦉🔌

*Hoot! Let me help [[You]] connect the owl's [[Intelligence]] to the wider world through MCP.*

[[Model Context Protocol]] (MCP) [[Servers]] extend [[Claude Code]]'s [[Capabilities]]. [[Obsidian Scribe]] uses **smoking-[[Mirror]]** for [[Vault Intelligence]].

## [[What]] is smoking-mirror?

smoking-mirror is an MCP server that provides:
- 📊 Real-time [[Vault]] [[Graph]] analysis
- 🔗 Backlink and forward [[Link]] tracking
- 🔍 [[Orphan]] [[Note]] [[Detection]]
- 🧠 [[Knowledge]] gap identification
- 📈 Link density patterns

**15 vault-* [[Skills]]** depend on [[This]] server.

## [[When]] Do You [[Need]] It?

### With smoking-mirror ([[Full]] Intelligence)

[[All]] 20+ skills [[Available]]:
- ✅ `/vault-health` - Comprehensive diagnostics
- ✅ `/vault-orphans` - Find isolated [[Notes]]
- ✅ `/vault-hubs` - Find highly connected notes
- ✅ `/vault-fix-links` - Repair broken [[Wikilinks]]
- ✅ *...and 11 more vault-* skills!*

### Without smoking-mirror ([[Core]] [[Features]] [[Only]])

5 skills still work:
- ✅ `/auto-log` - Daily [[Logging]]
- ✅ `/task-add` - Task [[Management]]
- ✅ `/rollup` - Periodic summarization
- ✅ `/rebuild-wikilink-cache` - [[Wikilink]] cache
- ✅ `/wikilink-apply` - [[Apply]] wikilink [[Suggestions]]

*The owl can still help, [[But]] its full wisdom requires smoking-mirror.*

## Configuration by Platform

### [[WSL]] (Ubuntu)

**[[Location]]:** [[Project]] `.mcp.json` in your vault directory

```json
{
  "mcpServers": {
    "smoking-mirror": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "smoking-mirror@latest"],
      "env": {
        "OBSIDIAN_VAULT_PATH": "/mnt/c/Users/YOUR_USERNAME/obsidian/YOUR_VAULT"
      }
    }
  }
}
```

**Path Format:** `/mnt/c/...` for Windows drives in WSL

### Windows

**Location:** Global `C:\Users\YOUR_USERNAME\.[[Claude]].json`

```json
{
  "mcpServers": { /* user-level servers */ },
  "projects": {
    "C:/Users/YOUR_USERNAME/obsidian/YOUR_VAULT": {
      "mcpServers": {
        "smoking-mirror": {
          "type": "stdio",
          "command": "cmd",
          "args": ["/c", "npx", "-y", "smoking-mirror@latest"],
          "env": {
            "OBSIDIAN_VAULT_PATH": "C:/Users/YOUR_USERNAME/obsidian/YOUR_VAULT"
          }
        }
      }
    }
  }
}
```

**CRITICAL:**
- Use `cmd /c npx` wrapper (not direct `npx`)
- Project key uses forward slashes: `C:/Users/...`
- Path values use forward slashes

## Verification

### Check MCP Tools Are Available

```bash
# In your vault directory
claude tools
```

Look for smoking-mirror tools:
```
mcp__smoking-mirror__get_backlinks
mcp__smoking-mirror__find_orphan_notes
mcp__smoking-mirror__get_vault_stats
mcp__smoking-mirror__search_notes
...
```

*If you see these, the owl's intelligence network is active!* 🦉

### Test a Vault Skill

```bash
/vault-health
```

Should show comprehensive vault statistics.

## Multiple MCP Servers

smoking-mirror works alongside other MCP servers:

```json
{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    },
    "smoking-mirror": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "smoking-mirror@latest"],
      "env": {
        "OBSIDIAN_VAULT_PATH": "/path/to/vault"
      }
    }
  }
}
```

*The owl plays well with others!*

## Troubleshooting

### "MCP server not found"

**Check:**
1. `npx` is installed: `npm install -g npx`
2. Path to vault is correct and absolute
3. Path format matches your platform (WSL vs Windows)

### "Connection closed" (Windows)

You're missing the `cmd /c` wrapper:

```json
{
  "command": "cmd",  // ← Add this
  "args": ["/c", "npx", "-y", "smoking-mirror@latest"]  // ← Add "/c"
}
```

### Skills still show "requires MCP"

**Restart Claude Code after adding MCP config:**

```bash
# Exit Claude Code
# Restart in vault directory
cd /path/to/vault
claude
```

### Vault path issues

**Ensure path is absolute:**
- ✅ `/mnt/c/Users/benca/[[Obsidian]]/Ben`
- ✅ `C:/Users/benca/obsidian/Ben`
- ❌ `~/obsidian/Ben` (relative paths don't work)
- ❌ `../Ben` (relative paths don't work)

## Advanced: Custom MCP Config

### User-Level vs Project-Level

| Level | Scope | Config Location |
|-------|-------|-----------------|
| **User** | All projects | `~/.claude.json` or `C:\Users\...\.claude.json` |
| **Project** | One vault | `.mcp.json` in vault root |

**Recommendation:**
- User-level for global servers (github, playwright)
- Project-level for vault-specific (smoking-mirror)

### Environment Variables

smoking-mirror supports:

```json
{
  "env": {
    "OBSIDIAN_VAULT_PATH": "/path/to/vault",
    "LOG_LEVEL": "debug"  // Optional: for troubleshooting
  }
}
```

## [[Next]] Steps

With MCP configured, the owl's full intelligence awakens:

- **[Vault Intelligence Guide](../features/vault-intelligence.md)** - [[Explore]] 15 vault-* skills
- **[Vault Analysis Example](../examples/vault-analysis.md)** - [[See]] it in [[Action]]
- **[Getting Started](../getting-started.md)** - If you're new here

*The owl's eyes glow brighter with [[Each]] connection, dear scholar!* 🦉✨
