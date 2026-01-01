(div align="center")

(img src="docs/assets/logo-alt.png" alt="[[Obsidian Scribe]]" width="280")

### Unlock Deeper [[Insights]] in Your [[Knowledge]] [[Vault]]

*A wise owl companion for [[Obsidian]] vault [[Automation]] and [[Intelligence]]*

[![License: MIT](https://img.shields.io/badge/License-MIT-gold.svg)](LICENSE)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-8B5CF6)](https://github.com/anthropics/claude-code)

(/div)

---

(img src="docs/assets/banner.png" alt="Obsidian [[Scribe]] in [[Action]]" width="100%")

## [[Features]]

(img src="docs/assets/[[Feature]]-icons.png" alt="Features" align="right" width="200")

- **[[Wikilink]] Automation** - [[Auto]]-[[Suggest]] and [[Apply]] `[[wikilinks]]` to your [[Notes]]
- **Periodic [[Note]] Rollups** - Chain daily → weekly → [[Monthly]] → [[Quarterly]] → yearly summaries
- **Vault Health [[Tools]]** - [[Orphan]] [[Detection]], broken [[Link]] repair, link density analysis
- **Privacy Protection** - [[Person Name]] format enforcement, protected folders

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
| **WSL** | Project `.[[Claude]]/settings.json` | `/mnt/c/...` | Checked into git |
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
3. Ensure obsidian-scribe path points to the repository root (contains `.claude-[[Plugin]]/`)
4. Look for errors in debug logs: `C:\Users\<you>\.claude\debug\`

### Plugin Version Updates

**After pushing a new version to GitHub**, the plugin won't automatically update. Follow these steps:

#### Standard Update Process

**On WSL:**
```bash
cd ~/.claude/plugins/marketplaces/obsidian-scribe && git pull origin main
claude plugin update --scope local obsidian-scribe@obsidian-scribe
# Restart Claude Code session to apply changes
```

**On Windows (PowerShell):**
```powershell
cd C:\Users\<YourUsername>\.claude\plugins\marketplaces\obsidian-scribe
git pull origin main
claude plugin update --scope local obsidian-scribe@obsidian-scribe
# Restart Claude Code session to apply changes
```

**Notes:**
- Command is `plugin` (singular), not `[[Plugins]]`
- `--[[Scope]] local` flag required for vault-scoped plugins
- Can update from either platform - plugin cache is shared
- Manual pull required - Claude Code doesn't auto-update from GitHub

#### Verification

Check that the update worked:

```bash
# Check installed version
cat ~/.claude/plugins/installed_plugins.json | grep -A 10 obsidian-scribe

# Verify marketplace version
cat ~/.claude/plugins/marketplaces/obsidian-scribe/plugins/obsidian-scribe/.claude-plugin/plugin.json | grep version

# After restart, check debug log
cat ~/.claude/debug/<session-id>.txt | grep "Found.*plugins"
```

Expected output after restart:
- `Found 2 plugins (2 enabled, 0 [[Disabled]])`
- `Loaded plugins - Enabled: 2`
- `Registered X [[Hooks]] from 2 plugins`

#### Important Notes

- **Command syntax**: `claude plugin` (singular), NOT `claude plugins`
- **Local scope**: Local-scoped plugins require `--scope local` flag
- **Auto-enabling**: Local-scoped plugins are automatically enabled after update
- **Manual pull required**: The marketplace clone does NOT auto-update from GitHub
- The `enable` command only works for disabled plugins, not for newly installed plugins

#### Troubleshooting

**Problem**: Plugin shows old version even after update

**Diagnosis:**
```bash
# Check if marketplace clone is stale
cd ~/.claude/plugins/marketplaces/obsidian-scribe && git log -1 --oneline

# Compare with GitHub
# Visit https://github.com/bencassie/obsidian-scribe/commits/main
```

**Solution**: If marketplace is behind, run the 3-step update process above.

**Problem**: Hooks not loading

**Check debug log:**
```bash
cat ~/.claude/debug/<latest-session-id>.txt | grep -E "Found|Registered|hooks"
```

If you see "Registered 0 hooks", the plugin version likely doesn't include the hooks configuration. Verify:
```bash
cat ~/.claude/plugins/cache/obsidian-scribe/obsidian-scribe/<version>/.claude-plugin/plugin.json | grep hooks
```

If missing, the cache has an old version. Re-run the update process.

#### Development Workflow

When developing the plugin:

1. Make changes and bump version in all 3 manifest files
2. Commit and push to GitHub
3. Run the standard update process (above)
4. Test in a fresh Claude session

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

[[This]] approach ensures [[WSL]] and [[Windows]] users can collaborate without conflicts.

## Plugins

Coming soon...

## License

MIT
