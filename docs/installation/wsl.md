# WSL (Ubuntu) Installation 🦉🐧

*Hoot! A Linux scholar! The owl appreciates your choice of perch.*

This Guide helps You set up Obsidian Scribe on WSL (Windows Subsystem for Linux).

## Prerequisites

### 1. Python Setup

WSL Ubuntu doesn't symlink `python` to `python3` by default, But the owl's Hooks Need it!

```bash
# Install the python symlink
sudo apt install python-is-python3

# Verify
python --version
# Should show: Python 3.x.x
```

*Without this, the owl's hooks won't be able to fly!*

### 2. Claude Code

Ensure Claude Code CLI is installed:

```bash
claude --version
```

## Installation Steps

### Step 1: Add the Marketplace

```bash
claude plugin marketplace add bencassie/obsidian-scribe
```

### Step 2: Install the Plugin

```bash
claude plugin install obsidian-scribe@obsidian-scribe
```

### Step 3: Verify Installation

```bash
claude skills | grep obsidian-scribe -A 30
```

*You should see 20+ skills! The owl's full wisdom is now at your disposal.*

## MCP Server Setup (Optional but Recommended)

The vault intelligence features (15 vault-* skills) require the smoking-mirror MCP server.

### Add to Your Project `.MCP.json`

Navigate to your vault directory and create/edit `.mcp.json`:

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

**Replace:**
- `YOUR_USERNAME` → Your Windows username
- `YOUR_VAULT` → Your vault folder name

**Path Format:** WSL uses `/mnt/c/` prefix for Windows drives.

### Verify MCP Server

```bash
# In your vault directory
claude tools

# Look for smoking-mirror tools like:
# - mcp__smoking-mirror__get_backlinks
# - mcp__smoking-mirror__find_orphan_notes
```

*If you see these, the owl's intelligence is fully activated!* 🦉

## Testing Your Installation

### Test Core Features

```bash
# In your vault with Claude Code
/auto-log Testing WSL installation with the wise owl

# Check vault health
/vault-health
```

### Test Hooks

Hooks run automatically, but you can test them manually:

```bash
cd /mnt/c/Users/.../obsidian-scribe/plugins/obsidian-scribe

# Test session start hook
python hooks/session-start.py

# Should show vault status
```

## Common Issues

### "python: command not found"

```bash
# Install the symlink
sudo apt install python-is-python3
```

### "MCP server not found"

Check your `.mcp.json`:
- Path uses `/mnt/c/...` format
- Vault path is absolute and correct
- `npx` command is available (`npm install -g npx`)

### Hooks not firing

Ensure:
- Python 3.8+ is installed
- `python` command works (not just `python3`)
- Hook files have execute permissions: `chmod +x hooks/*.py`

## Next Steps

Your perch is Prepared! Explore:
- **[Getting Started](../getting-started.md)** - First flights
- **[Daily Logging](../features/daily-logging.md)** - Capture your work
- **[Vault Intelligence](../features/vault-intelligence.md)** - Analyze your Vault

*The wise owl awaits your commands, dear Linux scholar!* 🦉✨
