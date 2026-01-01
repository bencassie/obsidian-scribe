# Windows Installation

Setup Obsidian Scribe on Windows (PowerShell).

---

## Prerequisites

### Python 3.8+

```powershell
python --version
# Should show: Python 3.x.x
```

If `python` doesn't work, install from [python.org](https://www.python.org/downloads/) and check "Add to PATH".

### Claude Code

```powershell
claude --version
```

---

## Installation

### Option 1: From GitHub (Recommended)

```powershell
/plugin marketplace add bencassie/obsidian-scribe
/plugin install obsidian-scribe@bencassie/obsidian-scribe
```

Or use the interactive UI: `/plugin` → Discover → obsidian-scribe → Install

### Option 2: Manual Configuration

Add to your global `C:\Users\<you>\.claude.json`:

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

**Replace:**
- `<you>` → Your Windows username
- `<vault>` → Your vault folder name

**Critical:** Use forward slashes `/` in all paths.

### Verify Installation

```powershell
cd C:/Users/<you>/obsidian/<vault>
claude

# Check skills loaded
/vault-health
```

---

## MCP Server Setup (Required for vault intelligence)

The 16 vault-* skills require smoking-mirror MCP.

### Windows npx Wrapper (Required)

On Windows, MCP servers using `npx` **must** be wrapped with `cmd /c`:

```json
{
  "command": "cmd",
  "args": ["/c", "npx", "-y", "smoking-mirror@latest"]
}
```

Direct `npx` fails with "Connection closed" errors on Windows.

### Full Configuration

Add to `C:\Users\<you>\.claude.json`:

```json
{
  "mcpServers": {
    "github": { /* ... */ },
    "playwright": { /* ... */ }
  },
  "projects": {
    "C:/Users/<you>/obsidian/<vault>": {
      "extraKnownMarketplaces": {
        "obsidian-scribe": {
          "source": {
            "source": "github",
            "repo": "bencassie/obsidian-scribe"
          }
        }
      },
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

### Verify MCP

```powershell
cd C:/Users/<you>/obsidian/<vault>
claude tools

# Look for smoking-mirror tools
```

---

## Testing

```powershell
# Test logging
/auto-log Testing Windows installation

# Test vault health (requires MCP)
/vault-health

# Test hooks
python C:\Users\<you>\src\obsidian-scribe\plugins\obsidian-scribe\hooks\session-start.py
```

---

## Troubleshooting

### "python: command not found"

Install Python from [python.org](https://www.python.org/downloads/) and check "Add to PATH".

### "MCP server connection closed"

Add the `cmd /c` wrapper:

```json
{
  "command": "cmd",
  "args": ["/c", "npx", "-y", "smoking-mirror@latest"]
}
```

### Path format confusion

Windows configs use **forward slashes**:
- ✅ `C:/Users/alice/obsidian/MyVault`
- ❌ `C:\\Users\\alice\\obsidian\\MyVault`
- ❌ `C:\Users\alice\obsidian\MyVault`

---

## Next Steps

- [Getting Started](../getting-started.md)
- [MCP Servers Guide](mcp-servers.md)
- [Skills Reference](../skills-reference.md)
