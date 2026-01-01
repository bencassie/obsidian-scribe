#!/usr/bin/env python3
"""
Claude Code Plugin/Hook Diagnostics
Run this in a fresh Claude Code session to diagnose plugin loading issues.

Usage:
  1. Start fresh Claude Code session in vault directory
  2. Run: python /path/to/diagnose-hooks.py
  3. Copy output and compare WSL vs Windows
"""

import json
import os
import platform
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ============================================================================
# CONFIGURATION - Update these paths for your setup
# ============================================================================

VAULT_PATH = Path(os.environ.get("OBSIDIAN_VAULT_PATH", Path.cwd()))
PLUGIN_PATH = Path("C:/Users/benca/src/obsidian-scribe/plugins/obsidian-scribe")
WSL_PLUGIN_PATH = Path("/mnt/c/Users/benca/src/obsidian-scribe/plugins/obsidian-scribe")

# ============================================================================
# DIAGNOSTICS
# ============================================================================

def header(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def section(title):
    print(f"\n--- {title} ---")

def check_environment():
    header("ENVIRONMENT")

    print(f"Platform:        {platform.system()} {platform.release()}")
    print(f"Python:          {sys.version}")
    print(f"CWD:             {Path.cwd()}")
    print(f"Home:            {Path.home()}")

    # Check if WSL
    is_wsl = "microsoft" in platform.uname().release.lower() or os.path.exists("/proc/version")
    if is_wsl:
        try:
            with open("/proc/version") as f:
                is_wsl = "microsoft" in f.read().lower()
        except:
            pass
    print(f"Is WSL:          {is_wsl}")

    # Claude Code env vars
    section("Claude Code Environment Variables")
    claude_vars = [k for k in os.environ if k.startswith(("CLAUDE", "ANTHROPIC"))]
    if claude_vars:
        for var in sorted(claude_vars):
            print(f"  {var}={os.environ[var]}")
    else:
        print("  (none set)")

    # Check CLAUDE_PLUGIN_ROOT specifically
    plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT")
    print(f"\n  CLAUDE_PLUGIN_ROOT: {plugin_root or '(not set)'}")

    return is_wsl

def check_config_files(is_wsl):
    header("CONFIGURATION FILES")

    if is_wsl:
        user_claude_json = Path.home() / ".claude.json"
        user_settings = Path.home() / ".claude" / "settings.json"
    else:
        user_claude_json = Path("C:/Users/benca/.claude.json")
        user_settings = Path("C:/Users/benca/.claude/settings.json")

    project_settings = Path.cwd() / ".claude" / "settings.json"

    files = [
        ("User .claude.json", user_claude_json),
        ("User settings.json", user_settings),
        ("Project settings.json", project_settings),
    ]

    for name, path in files:
        section(name)
        print(f"  Path: {path}")
        print(f"  Exists: {path.exists()}")

        if path.exists():
            try:
                data = json.loads(path.read_text(encoding='utf-8'))

                # Show relevant fields
                if "hooks" in data:
                    print(f"  hooks: {json.dumps(data['hooks'], indent=4)[:500]}")
                if "enabledPlugins" in data:
                    print(f"  enabledPlugins: {data['enabledPlugins']}")
                if "extraKnownMarketplaces" in data:
                    print(f"  extraKnownMarketplaces: {json.dumps(data['extraKnownMarketplaces'], indent=4)}")
            except Exception as e:
                print(f"  Error reading: {e}")

def check_plugin_structure(is_wsl):
    header("PLUGIN STRUCTURE")

    plugin_path = WSL_PLUGIN_PATH if is_wsl else PLUGIN_PATH
    print(f"Plugin path: {plugin_path}")
    print(f"Exists: {plugin_path.exists()}")

    if not plugin_path.exists():
        print("  ❌ Plugin directory not found!")
        return

    # Check required files
    required = [
        ".claude-plugin/plugin.json",
        ".claude-plugin/marketplace.json",
        "hooks/hooks.json",
    ]

    section("Required Files")
    for rel_path in required:
        full_path = plugin_path / rel_path
        status = "✅" if full_path.exists() else "❌"
        print(f"  {status} {rel_path}: {full_path.exists()}")

    # Show plugin.json content
    section("plugin.json")
    plugin_json = plugin_path / ".claude-plugin" / "plugin.json"
    if plugin_json.exists():
        try:
            data = json.loads(plugin_json.read_text(encoding='utf-8'))
            print(f"  name: {data.get('name')}")
            print(f"  version: {data.get('version')}")
            print(f"  hooks: {data.get('hooks')}")
            print(f"  skills: {data.get('skills')}")
            print(f"  agents: {data.get('agents')}")
        except Exception as e:
            print(f"  Error: {e}")

    # Show hooks.json content
    section("hooks.json")
    hooks_json = plugin_path / "hooks" / "hooks.json"
    if hooks_json.exists():
        try:
            data = json.loads(hooks_json.read_text(encoding='utf-8'))
            print(f"  description: {data.get('description', '(none)')}")
            hooks = data.get('hooks', {})
            for event, configs in hooks.items():
                print(f"  {event}:")
                for config in configs:
                    for hook in config.get('hooks', []):
                        cmd = hook.get('command', '(no command)')
                        print(f"    - {cmd[:80]}...")
        except Exception as e:
            print(f"  Error: {e}")

def check_wikilink_cache():
    header("WIKILINK CACHE STATUS")

    cache_file = Path.cwd() / ".claude" / "wikilink-entities.json"
    print(f"Cache file: {cache_file}")
    print(f"Exists: {cache_file.exists()}")

    if cache_file.exists():
        try:
            data = json.loads(cache_file.read_text(encoding='utf-8'))
            meta = data.get('_metadata', {})
            print(f"  generated_at: {meta.get('generated_at')}")
            print(f"  vault_path: {meta.get('vault_path')}")
            print(f"  generator: {meta.get('generator')}")
            print(f"  total_entities: {meta.get('total_entities')}")

            # Check if path looks like WSL or Windows
            vault_path = meta.get('vault_path', '')
            if vault_path.startswith('/mnt/'):
                print(f"  path_type: WSL")
            elif vault_path.startswith('C:') or vault_path.startswith('c:'):
                print(f"  path_type: Windows")
            else:
                print(f"  path_type: Unknown")
        except Exception as e:
            print(f"  Error: {e}")

def test_hook_execution(is_wsl):
    header("HOOK EXECUTION TEST")

    plugin_path = WSL_PLUGIN_PATH if is_wsl else PLUGIN_PATH
    hook_script = plugin_path / "hooks" / "session-start.py"

    print(f"Hook script: {hook_script}")
    print(f"Exists: {hook_script.exists()}")

    if not hook_script.exists():
        print("  ❌ Hook script not found!")
        return

    section("Direct Execution Test")
    try:
        result = subprocess.run(
            [sys.executable, str(hook_script)],
            cwd=str(Path.cwd()),
            capture_output=True,
            text=True,
            timeout=30
        )
        print(f"  Exit code: {result.returncode}")
        if result.stdout:
            # Parse JSON output
            try:
                output = json.loads(result.stdout)
                print(f"  Output: {json.dumps(output, indent=4)[:500]}")
            except:
                print(f"  Output: {result.stdout[:500]}")
        if result.stderr:
            print(f"  Stderr: {result.stderr[:300]}")
    except Exception as e:
        print(f"  Error: {e}")

    section("CLAUDE_PLUGIN_ROOT Expansion Test")
    # Test if variable expansion works
    test_cmd = 'python "${CLAUDE_PLUGIN_ROOT}/hooks/session-start.py"'
    print(f"  Command: {test_cmd}")
    print(f"  Note: This requires CLAUDE_PLUGIN_ROOT to be set by Claude Code")

    plugin_root = os.environ.get("CLAUDE_PLUGIN_ROOT")
    if plugin_root:
        expanded = test_cmd.replace("${CLAUDE_PLUGIN_ROOT}", plugin_root)
        print(f"  Expanded: {expanded}")
    else:
        print(f"  ⚠️  CLAUDE_PLUGIN_ROOT not set - plugin hooks won't work!")

def check_claude_commands():
    header("CLAUDE CODE COMMANDS TO RUN")

    print("""
Run these commands in your Claude Code session to check hook/plugin status:

  /hooks          - List all registered hooks
  /plugins        - List installed plugins
  /context        - Show loaded context including plugins
  /doctor         - Run diagnostics

Debug mode (run from terminal):
  claude --debug hooks     - See hook loading details
  claude --debug plugins   - See plugin loading details
  claude --debug '*'       - See all debug output
""")

def main():
    print(f"\n{'#'*60}")
    print(f"#  CLAUDE CODE HOOK/PLUGIN DIAGNOSTICS")
    print(f"#  Run: {datetime.now().isoformat()}")
    print(f"{'#'*60}")

    is_wsl = check_environment()
    check_config_files(is_wsl)
    check_plugin_structure(is_wsl)
    check_wikilink_cache()
    test_hook_execution(is_wsl)
    check_claude_commands()

    header("SUMMARY")
    print(f"""
Platform: {'WSL' if is_wsl else 'Windows'}
Timestamp: {datetime.now().isoformat()}

Next steps:
1. Run /hooks in Claude Code to see registered hooks
2. Run /plugins to see if obsidian-scribe is listed
3. Compare this output between WSL and Windows sessions
4. Check if CLAUDE_PLUGIN_ROOT is set during hook execution
""")

if __name__ == "__main__":
    main()
