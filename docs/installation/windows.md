# [[Windows]] Installation 🦉🪟

*Hoot! A Windows [[Scribe]]! Let me help [[You]] prepare your nest with care.*

[[This]] [[Guide]] covers [[Obsidian Scribe]] installation on Windows ([[PowerShell]]).

## Prerequisites

### 1. [[Python]] Setup

Ensure Python 3.8+ is installed and [[Available]] as `python`:

```powershell
# Verify Python is installed
python --version
# Should show: Python 3.x.x
```

If `python` command doesn't work, install from [python.org](https://www.python.org/downloads/) and ensure "Add to PATH" is checked.

### 2. Claude Code

Ensure Claude Code CLI is installed:

```powershell
claude --version
```

## Installation Steps

### Step 1: Add the Marketplace

```powershell
claude plugin marketplace add bencassie/obsidian-scribe
```

### Step 2: Install the Plugin

```powershell
claude plugin install obsidian-scribe@obsidian-scribe
```

### Step 3: Verify Installation

```powershell
claude skills

# Look for obsidian-scribe skills
```

*The owl should now be perched in your Claude Code installation!* 🦉

## MCP Server Setup (Optional but Recommended)

The vault intelligence features (15 vault-* skills) require smoking-mirror MCP.

### CRITICAL: Windows `npx` Wrapper

On Windows, MCP servers using `npx` **must** be wrapped with `cmd /c`:

```json
{
  "command": "cmd",
  "args": ["/c", "npx", "-y", "smoking-mirror@latest"]
}
```

Direct `npx` fails with "Connection closed" errors on Windows.

### Global `.[[Claude]].json` Configuration

The owl recommends using a global `.claude.json` with project-specific settings.

**Location:** `C:\Users\YOUR_USERNAME\.claude.json`

```json
{
  "mcpServers": {
    "github": { /* ... */ },
    "playwright": { /* ... */ }
  },
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

**Replace:**
- `YOUR_USERNAME` → Your Windows username
- `YOUR_VAULT` → Your vault folder name

**CRITICAL Notes:**
- Project key uses **forward slashes**: `C:/Users/...` (not `C:\\Users\\...`)
- Path values use **forward slashes**: `"OBSIDIAN_VAULT_PATH": "C:/Users/..."`
- Always use `cmd /c npx` wrapper on Windows

### Verify MCP Server

```powershell
# In your vault directory
claude tools

# Look for smoking-mirror tools
```

*If you see them, the owl's intelligence is ready to soar!* 🦉

## Testing Your Installation

### Test Core Features

```powershell
# In your vault with Claude Code
/auto-log Testing Windows installation

# Check vault health
/vault-health
```

### Test Hooks (PowerShell)

```powershell
cd C:\Users\...\obsidian-scribe\plugins\obsidian-scribe

# Test session start hook
python hooks\session-start.py

# Should show vault status
```

## Common Issues

### "python: command not found"

Install Python from [python.org](https://www.python.org/downloads/) and check "Add to PATH" during installation.

### "MCP server connection closed"

You forgot the `cmd /c` wrapper! Update your config:

```json
{
  "command": "cmd",
  "args": ["/c", "npx", "-y", "smoking-mirror@latest"]
}
```

### Hooks not working

Ensure:
- Python 3.8+ installed
- `python` command works (check with `python --version`)
- Paths use forward slashes in configs

### Path format confusion

**Windows configs use forward slashes:**
- ✅ `C:/Users/benca/[[Obsidian]]/Ben`
- ❌ `C:\\Users\\benca\\obsidian\\Ben`
- ❌ `C:\Users\benca\obsidian\Ben`

## [[Next]] Steps

Your Windows perch is [[Ready]]! [[Explore]]:
- **[Getting Started](../getting-started.md)** - Begin your journey
- **[MCP Servers Guide](mcp-servers.md)** - [[Deep]] [[Dive]] into configuration
- **[Daily Logging](../features/daily-logging.md)** - Start capturing work

*The wise owl is ready to assist, dear Windows scribe!* 🦉✨
