<div align="center">

<img src="docs/assets/logo-alt.png" alt="Obsidian Scribe" width="280">

### Unlock Deeper Insights in Your Knowledge Vault

*A wise owl companion for Obsidian vault automation and intelligence*

[![License: MIT](https://img.shields.io/badge/License-MIT-gold.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-8B5CF6)](https://github.com/anthropics/claude-code)

</div>

---

<img src="docs/assets/banner.png" alt="Obsidian Scribe in action" width="100%">

## Features

<img src="docs/assets/feature-icons.png" alt="Features" align="right" width="200">

- **Wikilink Automation** - Auto-suggest and apply `[[wikilinks]]` to your notes
- **Periodic Note Rollups** - Chain daily → weekly → monthly → quarterly → yearly summaries
- **Vault Health Tools** - Orphan detection, broken link repair, link density analysis
- **Privacy Protection** - Person name format enforcement, protected folders

## Installation

```bash
/plugin marketplace add bencassie/obsidian-scribe
```

## Multi-Platform Configuration

**CRITICAL**: This plugin is designed to work seamlessly across WSL and Windows using dual-config architecture.

### The Pattern

All platform-specific configurations follow the same pattern to enable cross-platform collaboration:

| Platform | Configuration Location | Path Format | Status |
|----------|------------------------|-------------|--------|
| **WSL** | Project `.claude/settings.json` | `/mnt/c/...` | Checked into git |
| **Windows** | Global `.claude.json` project override | `C:/...` | Local only (not committed) |

### Why This Matters

- **Team Collaboration**: WSL users commit configs that work for them; Windows users override locally
- **No Environment Variables**: Platform differences handled through config structure
- **Single Source of Truth**: WSL config in git; Windows overrides stay local
- **Automatic Switching**: Claude Code automatically uses the right config for your platform

### Windows Setup (Step-by-Step)

**1. Locate your global config file:**
   - Path: `C:\Users\<YourUsername>\.claude.json`
   - Example: `C:\Users\alice\.claude.json`
   - This file is in your Windows user directory (NOT in the vault)

**2. Open the file in a text editor** (VSCode, Notepad++, etc.)

**3. Find or create the `projects` section:**
   - Look for `"projects": {` in the file
   - If it doesn't exist, add it after the `mcpServers` section (or at the end before the final `}`)

**4. Add your vault configuration:**

Replace the placeholders with your actual paths:

```json
{
  "projects": {
    "C:/Users/<YourUsername>/obsidian/<YourVaultName>": {
      "extraKnownMarketplaces": {
        "obsidian-scribe": {
          "source": {
            "source": "directory",
            "path": "C:/Users/<YourUsername>/src/obsidian-scribe"
          }
        }
      }
    }
  }
}
```

**Example with real values:**

```json
{
  "projects": {
    "C:/Users/alice/obsidian/MyVault": {
      "extraKnownMarketplaces": {
        "obsidian-scribe": {
          "source": {
            "source": "directory",
            "path": "C:/Users/alice/src/obsidian-scribe"
          }
        }
      }
    }
  }
}
```

**5. If you already have other projects configured:**

Add the new vault entry inside the existing `projects` object:

```json
{
  "projects": {
    "C:/Users/alice/src/other-project": {
      // ... existing config ...
    },
    "C:/Users/alice/obsidian/MyVault": {
      "extraKnownMarketplaces": {
        "obsidian-scribe": {
          "source": {
            "source": "directory",
            "path": "C:/Users/alice/src/obsidian-scribe"
          }
        }
      }
    }
  }
}
```

**6. Save the file and restart Claude Code**

**Critical Notes:**
- Use forward slashes `/` in ALL paths (not backslashes `\`)
- Project key must match your vault's full path: `C:/Users/.../obsidian/VaultName`
- Plugin path must match where you cloned obsidian-scribe
- NEVER modify `.claude/settings.json` with Windows paths (it breaks WSL)
- The global `.claude.json` is gitignored - Windows configs stay local

**Troubleshooting:**

If plugins don't load:
1. Verify paths use forward slashes: `C:/Users/...` not `C:\Users\...`
2. Check vault path matches exactly (use `pwd` in your vault directory)
3. Ensure obsidian-scribe path points to the repository root (contains `.claude-plugin/`)
4. Look for errors in debug logs: `C:\Users\<you>\.claude\debug\`

### Plugin Version Updates

If the plugin is stuck on an old version after updates:

**Symptom**: `~/.claude/plugins/installed_plugins.json` shows old version even though GitHub has newer version.

**Root Cause**: Marketplace source configured as `directory` instead of `github`, preventing auto-updates.

**Solution**:

1. **Check marketplace source:**
   ```bash
   cat ~/.claude/plugins/known_marketplaces.json | grep -A 5 obsidian-scribe
   ```

2. **If it shows `"source": "directory"`, switch to GitHub source:**

   Edit `~/.claude/plugins/known_marketplaces.json`:
   ```json
   "obsidian-scribe": {
     "source": {
       "source": "github",
       "owner": "bencassie",
       "repo": "obsidian-scribe"
     },
     "installLocation": "/home/ben/.claude/plugins/marketplaces/obsidian-scribe",
     "lastUpdated": "2026-01-01T10:14:00.000Z"
   }
   ```

3. **Update installed plugin registry** (`~/.claude/plugins/installed_plugins.json`):
   - Change `version` to latest (e.g., "1.0.11")
   - Change `installPath` to match new version
   - Change `gitCommitSha` to latest commit from GitHub
   - Update `lastUpdated` timestamp

4. **Create cache directory and copy latest files:**
   ```bash
   mkdir -p ~/.claude/plugins/cache/obsidian-scribe/obsidian-scribe/1.0.11
   cp -r /path/to/obsidian-scribe/plugins/obsidian-scribe/* \
     ~/.claude/plugins/cache/obsidian-scribe/obsidian-scribe/1.0.11/
   ```

5. **Restart Claude Code session**

**Prevention**: Always use GitHub source for automatic updates:
```bash
claude plugins add bencassie/obsidian-scribe
```

### WSL Setup

WSL users can commit plugin configuration directly to `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "obsidian-scribe": {
      "source": {
        "source": "directory",
        "path": "/mnt/c/Users/<you>/src/obsidian-scribe"
      }
    }
  }
}
```

This approach ensures WSL and Windows users can collaborate without conflicts.

## Plugins

Coming soon...

## License

MIT
