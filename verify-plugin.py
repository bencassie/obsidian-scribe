#!/usr/bin/env python3
"""
Verification script for obsidian-scribe plugin configuration
Tests both WSL and Windows path configurations
"""

import json
import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

# Detect platform
IS_WSL = 'microsoft' in os.uname().release.lower()
IS_WINDOWS = sys.platform == 'win32'

print("=" * 70)
print("  OBSIDIAN-SCRIBE PLUGIN VERIFICATION")
print(f"  Platform: {'WSL' if IS_WSL else 'Windows' if IS_WINDOWS else 'Linux'}")
print(f"  Time: {datetime.now().isoformat()}")
print("=" * 70)

# Define paths based on platform
if IS_WSL:
    VAULT_PATH = Path("/mnt/c/Users/benca/obsidian/Ben")
    PLUGIN_PATH = Path("/mnt/c/Users/benca/src/obsidian-scribe/plugins/obsidian-scribe")
    SETTINGS_FILE = VAULT_PATH / ".claude/settings.local.json"
    PYTHON_CMD = "python3"
elif IS_WINDOWS:
    VAULT_PATH = Path("C:/Users/benca/obsidian/Ben")
    PLUGIN_PATH = Path("C:/Users/benca/src/obsidian-scribe/plugins/obsidian-scribe")
    SETTINGS_FILE = VAULT_PATH / ".claude/settings.json"
    PYTHON_CMD = "python"
else:
    print("❌ Unsupported platform")
    sys.exit(1)

CACHE_FILE = VAULT_PATH / ".claude/wikilink-entities.json"

def test_paths():
    """Test that all required paths exist"""
    print("\n[1] PATH EXISTENCE TESTS")
    print("-" * 70)

    tests = {
        "Vault directory": VAULT_PATH,
        "Plugin directory": PLUGIN_PATH,
        "Settings file": SETTINGS_FILE,
        "Wikilink cache": CACHE_FILE,
        "Plugin.json": PLUGIN_PATH / ".claude-plugin/plugin.json",
        "Hooks.json": PLUGIN_PATH / "hooks/hooks.json",
        "Session-start hook": PLUGIN_PATH / "hooks/session-start.py",
        "Syntax-validate hook": PLUGIN_PATH / "hooks/syntax-validate.py",
        "Wikilink-suggest hook": PLUGIN_PATH / "hooks/wikilink-suggest.py",
        "Achievement-detect hook": PLUGIN_PATH / "hooks/achievement-detect.py"
    }

    all_exist = True
    for name, path in tests.items():
        exists = path.exists()
        status = "✅" if exists else "❌"
        print(f"  {status} {name}: {path}")
        if not exists:
            all_exist = False

    return all_exist

def test_settings():
    """Test settings configuration"""
    print("\n[2] SETTINGS CONFIGURATION TEST")
    print("-" * 70)

    if not SETTINGS_FILE.exists():
        print(f"  ❌ Settings file not found: {SETTINGS_FILE}")
        return False

    with open(SETTINGS_FILE) as f:
        settings = json.load(f)

    # Check plugin marketplace
    marketplaces = settings.get("extraKnownMarketplaces", {})
    scribe_marketplace = marketplaces.get("obsidian-scribe", {})
    plugin_path = scribe_marketplace.get("source", {}).get("path")

    print(f"  Plugin marketplace path: {plugin_path}")

    # Verify path format matches platform
    if IS_WSL:
        expected_prefix = "/mnt/c/"
        if plugin_path and plugin_path.startswith(expected_prefix):
            print(f"  ✅ Path format correct for WSL")
            path_ok = True
        else:
            print(f"  ❌ Path should start with '{expected_prefix}' for WSL")
            path_ok = False
    elif IS_WINDOWS:
        expected_prefix = "C:/"
        if plugin_path and plugin_path.startswith(expected_prefix):
            print(f"  ✅ Path format correct for Windows")
            path_ok = True
        else:
            print(f"  ❌ Path should start with '{expected_prefix}' for Windows")
            path_ok = False

    # Check if plugin is enabled
    enabled_plugins = settings.get("enabledPlugins", {})
    is_enabled = enabled_plugins.get("obsidian-scribe@obsidian-scribe", False)
    print(f"  {'✅' if is_enabled else '❌'} Plugin enabled: {is_enabled}")

    # Check permissions for CLAUDE_PLUGIN_ROOT
    permissions = settings.get("permissions", {}).get("allow", [])
    plugin_root_perms = [p for p in permissions if "CLAUDE_PLUGIN_ROOT" in p]

    if plugin_root_perms:
        print(f"  ✅ CLAUDE_PLUGIN_ROOT permission found:")
        for perm in plugin_root_perms:
            print(f"      {perm}")

        # Verify path in permission
        for perm in plugin_root_perms:
            if IS_WSL and "/mnt/c/" in perm:
                print(f"  ✅ Permission uses WSL path format")
                perm_ok = True
                break
            elif IS_WINDOWS and "C:/" in perm:
                print(f"  ✅ Permission uses Windows path format")
                perm_ok = True
                break
        else:
            print(f"  ❌ Permission path format doesn't match platform")
            perm_ok = False
    else:
        print(f"  ❌ CLAUDE_PLUGIN_ROOT permission not found")
        perm_ok = False

    return path_ok and is_enabled and perm_ok

def test_hook_execution():
    """Test direct hook execution"""
    print("\n[3] HOOK EXECUTION TEST")
    print("-" * 70)

    hook_script = PLUGIN_PATH / "hooks/session-start.py"

    if not hook_script.exists():
        print(f"  ❌ Hook script not found: {hook_script}")
        return False

    # Set environment variables
    env = os.environ.copy()
    env["CLAUDE_PLUGIN_ROOT"] = str(PLUGIN_PATH)
    env["OBSIDIAN_VAULT_PATH"] = str(VAULT_PATH)

    try:
        result = subprocess.run(
            [PYTHON_CMD, str(hook_script)],
            env=env,
            capture_output=True,
            text=True,
            timeout=10
        )

        print(f"  Exit code: {result.returncode}")

        if result.returncode == 0:
            print(f"  ✅ Hook executed successfully")

            # Try to parse output as JSON
            try:
                output = json.loads(result.stdout)
                context = output.get("hookSpecificOutput", {}).get("additionalContext", "")

                # Show first 200 chars of output
                preview = context[:200].strip()
                if preview:
                    print(f"\n  Output preview:")
                    for line in preview.split('\n')[:5]:
                        print(f"    {line}")
                    if len(context) > 200:
                        print(f"    ... ({len(context)} chars total)")

                return True
            except json.JSONDecodeError:
                print(f"  ⚠️  Output is not JSON format")
                print(f"  Output: {result.stdout[:200]}")
                return True  # Still counts as success if exit code is 0
        else:
            print(f"  ❌ Hook execution failed")
            print(f"  Stderr: {result.stderr}")
            return False

    except subprocess.TimeoutExpired:
        print(f"  ❌ Hook execution timed out")
        return False
    except Exception as e:
        print(f"  ❌ Hook execution error: {e}")
        return False

def test_wikilink_cache():
    """Test wikilink cache status"""
    print("\n[4] WIKILINK CACHE TEST")
    print("-" * 70)

    if not CACHE_FILE.exists():
        print(f"  ⚠️  Cache file does not exist: {CACHE_FILE}")
        print(f"  (This is OK if cache hasn't been generated yet)")
        return True

    with open(CACHE_FILE) as f:
        cache = json.load(f)

    metadata = cache.get("_metadata", {})

    print(f"  Generated: {metadata.get('generated_at')}")
    print(f"  Generator: {metadata.get('generator')}")
    print(f"  Vault path: {metadata.get('vault_path')}")
    print(f"  Entities: {metadata.get('total_entities')}")
    print(f"  Path type: {metadata.get('path_type')}")

    # Check if cache is recent (within last hour)
    gen_time_str = metadata.get('generated_at', '')
    if gen_time_str:
        try:
            gen_time = datetime.fromisoformat(gen_time_str)
            age_seconds = (datetime.now() - gen_time).total_seconds()
            age_minutes = age_seconds / 60

            if age_minutes < 60:
                print(f"  ✅ Cache is fresh ({age_minutes:.1f} minutes old)")
            else:
                print(f"  ⚠️  Cache is stale ({age_minutes/60:.1f} hours old)")
        except ValueError:
            print(f"  ⚠️  Cannot parse cache timestamp")

    # Check if generator is obsidian-scribe
    if metadata.get('generator', '').startswith('obsidian-scribe'):
        print(f"  ✅ Cache generated by obsidian-scribe plugin")
        return True
    else:
        print(f"  ⚠️  Cache not generated by obsidian-scribe")
        return True  # Not critical

def main():
    """Run all verification tests"""

    results = {
        "Paths": test_paths(),
        "Settings": test_settings(),
        "Hook Execution": test_hook_execution(),
        "Cache": test_wikilink_cache()
    }

    print("\n" + "=" * 70)
    print("  SUMMARY")
    print("=" * 70)

    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {status}: {test_name}")

    all_passed = all(results.values())

    print("\n" + "=" * 70)
    if all_passed:
        print("  ✅ ALL TESTS PASSED - Plugin should work correctly")
    else:
        print("  ❌ SOME TESTS FAILED - Review errors above")
    print("=" * 70)

    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
