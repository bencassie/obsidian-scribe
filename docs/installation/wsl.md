# WSL (Ubuntu) Installation

Setup Obsidian Scribe on WSL (Windows Subsystem for Linux).

---

## Prerequisites

### Python 3.8+

WSL Ubuntu doesn't symlink `python` to `python3` by default:

```bash
# Install the python symlink
sudo apt install python-is-python3

# Verify
python --version
# Should show: Python 3.x.x
```

### Claude Code

```bash
claude --version
```

---

## Installation

### Option 1: From GitHub (Recommended)

```bash
/install bencassie/obsidian-scribe
```

### Option 2: Manual Configuration

Add to your project's `.claude/settings.json`:

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

This config can be committed to git (works for all WSL users).

### Verify Installation

```bash
cd /mnt/c/Users/<you>/obsidian/<vault>
claude

# Check skills loaded
/vault-health
```

---

## MCP Server Setup (Required for vault intelligence)

The 16 vault-* skills require smoking-mirror MCP.

### Add to `.mcp.json`

In your vault directory, create/edit `.mcp.json`:

```json
{
  "mcpServers": {
    "smoking-mirror": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "smoking-mirror@latest"],
      "env": {
        "OBSIDIAN_VAULT_PATH": "/mnt/c/Users/<you>/obsidian/<vault>"
      }
    }
  }
}
```

**Path Format:** WSL uses `/mnt/c/` prefix for Windows drives.

### Verify MCP

```bash
claude tools

# Look for smoking-mirror tools like:
# - mcp__smoking-mirror__get_backlinks
# - mcp__smoking-mirror__find_orphan_notes
```

---

## Testing

```bash
# Test logging
/auto-log Testing WSL installation

# Test vault health (requires MCP)
/vault-health

# Test hooks
python /mnt/c/Users/.../obsidian-scribe/plugins/obsidian-scribe/hooks/session-start.py
```

---

## Troubleshooting

### "python: command not found"

```bash
sudo apt install python-is-python3
```

### "MCP server not found"

Check your `.mcp.json`:

- Path uses `/mnt/c/...` format
- Vault path is absolute and correct
- `npx` command is available (`npm install -g npx`)

### Hooks not firing

Ensure:

- Python 3.8+ installed
- `python` command works (not just `python3`)
- Hook files have execute permissions: `chmod +x hooks/*.py`

---

## Next Steps

- [Getting Started](../getting-started.md)
- [MCP Servers Guide](mcp-servers.md)
- [Skills Reference](../skills-reference.md)
