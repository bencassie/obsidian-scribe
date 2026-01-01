# [[Getting]] Started with [[Obsidian Scribe]] 🦉

*Hoot hoot! Welcome to the nest, young scholar. Let me [[Guide]] [[You]] on your journey to a wiser [[Vault]].*

## [[What]] is [[Obsidian]] [[Scribe]]?

Imagine having a wise owl perched beside your Obsidian vault, quietly helping you:
- 📝 [[Log]] your daily work with timestamps
- 🔗 Automatically [[Suggest]] [[Wikilinks]] as you write
- 📊 Summarize [[Weeks]] into months, months into quarters
- 🧠 [[Analyze]] your [[Knowledge]] [[Graph]] for [[Insights]]
- 🏆 [[Track]] your [[Achievements]] without lifting a feather

That's Obsidian Scribe - your [[Automated]] knowledge companion for [[Claude Code]].

## Prerequisites

Before we prepare your perch, ensure you [[Have]]:

- ✅ **Obsidian** - Your vault where knowledge roosts
- ✅ **[[Claude]] Code** - The CLI tool (install from [claude.com/code](https://claude.com/code))
- ✅ **[[Python]] 3.8+** - The owl's scripting [[Language]]
  - [[WSL]]: [[Run]] `sudo apt install python-is-python3`
  - [[Windows]]: Ensure `python` [[Command]] works

## Quick Installation

### Step 1: Add the [[Marketplace]]

Obsidian Scribe lives in a marketplace that Claude Code can access:

```bash
# Add the marketplace
claude plugin marketplace add bencassie/obsidian-scribe
```

*The owl rustles its feathers excitedly...*

### Step 2: Install the Plugin

```bash
# Install obsidian-scribe from the marketplace
claude plugin install obsidian-scribe@obsidian-scribe
```

### Step 3: Verify Installation

```bash
# Check that the plugin is installed
claude skills

# You should see 20+ skills listed!
```

*Hoot! If you see skills like `/vault-health` and `/auto-log`, you're ready to fly!*

## Essential Configuration

### For Vault Intelligence Features

Many of the owl's wisest skills require the smoking-mirror MCP server (15 vault-* skills depend on it).

**Platform-specific setup:**
- **[WSL Installation](installation/wsl.md)** - Linux scholars, this way please
- **[Windows Installation](installation/windows.md)** - Windows scribes, follow me
- **[MCP Server Setup](installation/mcp-servers.md)** - Detailed configuration

*Don't worry if you skip this - core features work without it! But the owl's intelligence truly shines with smoking-mirror enabled.*

## Your First Flight 🦉

Let's take Obsidian Scribe for a test flight!

### 1. Check Vault Health

```bash
/vault-health
```

*The owl scans your vault and reports back with wisdom about your knowledge nest.*

### 2. Log Something

```bash
/auto-log Tested Obsidian Scribe for the first time!
```

*The owl adds this to your daily note with a timestamp. Magnificent!*

### 3. Find Orphan Notes

```bash
/vault-orphans
```

*The owl identifies [[Notes]] that have no connections - lonely pages seeking [[Links]].*

## What's [[Next]]?

[[Now]] that you've spread your wings, [[Explore]] the owl's [[Full]] wisdom:

### By [[Use]] Case

- **Daily [[Logging]]** → [Daily Logging Guide](features/daily-logging.md)
- **[[Link]] [[Management]]** → [Wikilinks Guide](features/wikilinks.md)
- **Periodic summaries** → [Rollup Guide](features/rollup.md)
- **Vault analysis** → [Vault Intelligence](features/vault-intelligence.md)
- **Track [[Wins]]** → [Achievements Guide](features/achievements.md)

### [[Workflows]] & [[Examples]]

- 📅 [Daily Workflow](examples/daily-workflow.md) - How the owl helps throughout your day
- 🔍 [Vault Analysis](examples/vault-analysis.md) - Health [[Checks]] and [[Optimization]]
- 📊 [Rollup Chain](examples/rollup-chain.md) - Automated summarization

## [[Need]] Help?

*Even the wisest owl needs a helping wing sometimes!*

- 📖 Browse the [feature docs](features/) for detailed guides
- 🐛 [Report issues](https://github.com/bencassie/obsidian-scribe/issues) if something's amiss
- 💡 [Suggest features](https://github.com/bencassie/obsidian-scribe/discussions) you'd like to [[See]]

---

*"The journey of a thousand notes begins with a single link. Let's make yours magnificent together, dear scholar."* 🦉

**- Your Sage Owl Scribe**
