---
# This is an EXAMPLE/INFORMATIONAL rule file
# Copy this to your vault's .claude/rules/ directory if you want platform reminders

# Claude Code scoping
alwaysApply: true

# Obsidian metadata (optional - for vault organization)
type: rule
tags:
  - rule
  - platform
  - requirements
  - setup
aliases:
  - Platform Requirements
  - obsidian-scribe Platform Setup
date: 2026-01-01
description: Platform-specific requirements for obsidian-scribe plugin
---

# Platform Requirements (Informational)

> **Note**: This documents platform-specific requirements for obsidian-scribe.
> If you encounter hook execution issues, check these requirements.

This rule documents platform-specific requirements for the obsidian-scribe plugin.

## WSL (Windows Subsystem for Linux)

### Python Symlink Requirement

**CRITICAL**: WSL Ubuntu does not have `python` symlinked to `python3` by default. obsidian-scribe requires it.

**Install the symlink:**
```bash
sudo apt install python-is-python3
```

**Why:** All obsidian-scribe hooks use `python` (not `python3`) for cross-platform compatibility with Windows. This package creates the necessary symlink.

**Verify installation:**
```bash
python --version
# Should show: Python 3.x.x
```

**If you see "command not found":**
- You're missing the python→python3 symlink
- Run `sudo apt install python-is-python3`
- Restart your terminal/Claude Code session

### Path Format

When running from WSL, all Windows paths use `/mnt/c/...` format:
- Vault: `/mnt/c/Users/username/path/to/vault`
- Plugin: `/mnt/c/Users/username/.claude/plugins/...`

### Environment Variables

Claude Code automatically sets:
- `${CLAUDE_PLUGIN_ROOT}`: Points to plugin directory (Unix format)
- Used in hook commands: `python "${CLAUDE_PLUGIN_ROOT}/hooks/session-start.py"`

## Windows

### Python Installation

Ensure Python 3.8+ is installed and available in PATH as `python`.

**Download from:**
- https://www.python.org/downloads/
- Or use `winget install Python.Python.3.12`

**Verify:**
```powershell
python --version
# Should show: Python 3.x.x
```

**If you see "command not found":**
- Python is not in your PATH
- Reinstall Python and check "Add Python to PATH" during installation
- Or manually add Python to your PATH environment variable

### Path Format

Standard Windows paths with forward slashes (in JSON config):
- Vault: `C:/Users/username/path/to/vault`
- Plugin: `C:/Users/username/.claude/plugins/...`

**Note**: Forward slashes work in JSON even on Windows. Use them to avoid escaping backslashes.

## Cross-Platform Hook Commands

All hooks use `python` (not `python3`) for consistency:

```json
{
  "type": "command",
  "command": "python \"${CLAUDE_PLUGIN_ROOT}/hooks/session-start.py\""
}
```

### Why `python` not `python3`?

- **Windows**: Only has `python` (python3 doesn't exist)
- **macOS**: Has both `python` and `python3` by default
- **Linux**: Requires `python-is-python3` package to create `python` symlink
- **Result**: Using `python` works on all platforms (with proper setup)

### Environment Variable

`${CLAUDE_PLUGIN_ROOT}` is set automatically by Claude Code:
- Points to the plugin's root directory
- Expands to correct path format for the platform
- Used in all hook commands for portability

## Troubleshooting

### Hooks Not Running (WSL)

**Symptoms:**
- Hooks show as registered but don't execute
- No output from hooks in debug logs
- "python: command not found" in error logs

**Solution:**
```bash
# Install python symlink
sudo apt install python-is-python3

# Verify
python --version

# Restart Claude Code session
```

### Hooks Not Running (Windows)

**Symptoms:**
- Hooks show as registered but don't execute
- "python: command not found" in error logs

**Solution:**
1. Install Python 3.8+ from python.org
2. During installation, check "Add Python to PATH"
3. Restart terminal/Claude Code
4. Verify: `python --version`

### Permission Errors (WSL)

**Symptoms:**
- "Permission denied" when running hooks
- Hook scripts aren't executable

**Solution:**
```bash
# Make hooks executable
chmod +x ~/.claude/plugins/marketplaces/obsidian-scribe/plugins/obsidian-scribe/hooks/*.py

# Or for local plugin
chmod +x path/to/obsidian-scribe/plugins/obsidian-scribe/hooks/*.py
```

## Verification

Check that everything is set up correctly:

### 1. Python Available

```bash
# All platforms
python --version
# Expected: Python 3.x.x (where x >= 8)
```

### 2. Hooks Registered

In Claude Code session:
```bash
# Check debug log
cat ~/.claude/debug/[session-id].txt | grep "obsidian-scribe"

# Look for:
# "Registered 4 hooks from obsidian-scribe"
```

### 3. Test Hook Execution

Create a test daily note and make an edit:
- If achievement-detect hook works, you'll see "✓ Auto-Added X Achievements" message
- If wikilink-suggest hook works, entity names will get [[brackets]] automatically

## Platform-Specific MCP Configuration

obsidian-scribe uses the smoking-mirror MCP server, which also has platform requirements:

### WSL
```json
{
  "mcpServers": {
    "smoking-mirror": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-smoking-mirror"]
    }
  }
}
```

### Windows
```json
{
  "mcpServers": {
    "smoking-mirror": {
      "command": "cmd",
      "args": ["/c", "npx", "-y", "@modelcontextprotocol/server-smoking-mirror"]
    }
  }
}
```

**Note**: Windows requires `cmd /c` wrapper for npx commands.

## Configuration Example

To use this rule in your vault:

1. **Copy to your vault**: `.claude/rules/platform-requirements.md`
2. **Set `alwaysApply: true`** to get reminders across all files
3. **Check platform setup** using verification steps above

This rule serves as a reference for troubleshooting platform-specific issues.

## Related Documentation

- [Installation Guide](../installation/README.md)
- [Troubleshooting Guide](../installation/troubleshooting.md)
- [Hook Configuration](../../plugins/obsidian-scribe/hooks/hooks.json)
- [Cross-Platform Setup Guide](../../CLAUDE.md.example)
