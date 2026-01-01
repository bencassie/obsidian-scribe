# Skills Reference

Complete reference for all 33 skills in Obsidian Scribe. Each skill shows **how you actually ask** (natural language), **what Claude does**, and **what changes in your vault**.

---

## Daily Capture

### auto-log

Add timestamped entries to your daily note.

**User Story**: As a daily note user, I want to quickly log activities without leaving my workflow.

**You say:**
> "Log that I fixed the authentication bug"
> "Add to my daily: deployed v2.1 to production"
> "Note: meeting with Sarah about Q1 roadmap"
> "Put in my log: finished the API refactor"
> "Daily note: shipped the new dashboard"

**Claude does:**
- Opens today's daily note (creates if missing)
- Finds the `## Log` section
- Appends timestamped entry at the bottom

**Your daily note:**

```markdown
## Log
- 14:32 Fixed the authentication bug
- 15:45 Deployed v2.1 to production
- 16:00 Meeting with Sarah about Q1 roadmap
```

**Changes files:** Yes - appends to daily note

---

### task-add

Create tasks with natural language due dates.

**You say:**
> "Add a task: review PR #123 by tomorrow"
> "Task: finish quarterly report by January 15th"
> "Remind me to call the client by Friday"
> "Add todo: update the roadmap by end of week"
> "New task: deploy hotfix by EOD"

**Claude does:**
- Parses natural language date ("tomorrow", "Friday", "end of week")
- Converts to ISO date format
- Adds task to daily note's Tasks section

**Your daily note:**

```markdown
## Tasks
- [ ] Review PR #123 📅 2026-01-02
- [ ] Finish quarterly report 📅 2026-01-15
- [ ] Call the client 📅 2026-01-03
```

**Changes files:** Yes - appends to daily note

---

### food

Log food entries to your daily note.

**You say:**
> "Log food: chicken salad with quinoa"
> "I ate a burrito for lunch"
> "Food: oatmeal with berries for breakfast"
> "Add to my food log: coffee and a croissant"
> "Lunch was leftover pasta"

**Claude does:**
- Opens today's daily note
- Finds the Food section
- Appends the food entry

**Your daily note:**

```markdown
# Food
- Chicken salad with quinoa
- Burrito
- Oatmeal with berries
```

**Changes files:** Yes - appends to daily note

---

## Vault Health

All vault health skills are **read-only** - they analyze and report without changing your vault.

**Requires:** [smoking-mirror MCP](installation/mcp-servers.md)

### vault-health

Get a comprehensive vault diagnostic report.

**User Story**: As a vault maintainer, I want comprehensive vault statistics, so I can understand overall health.

**You say:**
> "How's my vault looking?"
> "Give me a vault health check"
> "What's the state of my knowledge base?"
> "Run vault diagnostics"
> "Analyze my vault"

**Claude does:**
- Queries smoking-mirror for vault statistics
- Analyzes link density, orphans, hubs
- Identifies knowledge gaps
- Compiles comprehensive report

**You get:**

```
🔍 Vault Health Report
Notes: 2,847
Links: 8,234 (2.89 avg/note)
Orphans: 43 (1.5%)
Hubs: 12 highly-connected notes

⚠️ Knowledge gaps detected:
- "API authentication" mentioned 15x, no dedicated note
- "Database optimization" mentioned 9x, undocumented
```

**Changes files:** No - read-only

---

### vault-stats

Quick numbers without deep analysis.

**You say:**
> "How many notes do I have?"
> "Vault stats"
> "Give me the numbers on my vault"
> "Quick vault summary"
> "What are my vault metrics?"

**Claude does:**
- Queries smoking-mirror for basic counts
- Returns totals without analysis

**You get:**

```
📊 Vault Stats
Notes: 2,847
Tags: 156 unique
Links: 8,234
Average links per note: 2.89
```

**Changes files:** No - read-only

---

### vault-orphans

Find notes with no incoming links (knowledge islands).

**User Story**: As a knowledge worker, I want to find orphaned notes, so I can integrate disconnected knowledge.

**You say:**
> "Find orphan notes"
> "What notes aren't linked to anything?"
> "Show me disconnected notes"
> "Which notes have no backlinks?"
> "Find knowledge islands"

**Claude does:**
- Queries smoking-mirror for notes with zero backlinks
- Returns list sorted by modification date

**You get:**

```
🏝️ Orphan Notes (43 found)
- tech/tools/obscure-library.md (3 months old)
- projects/abandoned-idea.md (6 months old)
- personal/random-thought.md (1 year old)
...
```

**Changes files:** No - read-only

---

### vault-hubs

Find your most connected notes (knowledge centers).

**User Story**: As a knowledge worker, I want to find my vault's most connected notes, so I can identify key concepts.

**You say:**
> "What are my hub notes?"
> "Find my most connected notes"
> "Which notes have the most backlinks?"
> "Show me knowledge centers"
> "What are my core concepts?"

**Claude does:**
- Queries smoking-mirror for notes with highest backlink counts
- Returns ranked list with connection counts

**You get:**

```
🌟 Hub Notes (top 12)
1. tech/frameworks/React.md (47 backlinks)
2. projects/Project Alpha.md (32 backlinks)
3. concepts/API Design.md (28 backlinks)
...
```

**Changes files:** No - read-only

---

### vault-gaps

Find topics mentioned frequently but lacking dedicated notes.

**You say:**
> "What topics am I missing notes for?"
> "Find knowledge gaps"
> "What concepts should I document?"
> "Show me undocumented topics"
> "What's mentioned but not linked?"

**Claude does:**
- Analyzes unlinked mentions across vault
- Identifies frequently-mentioned terms without dedicated notes
- Ranks by mention frequency

**You get:**

```
🦉 Knowledge Gaps Detected
"API Authentication" - mentioned 12 times, no note
"Database Optimization" - mentioned 8 times, no note
"Error Handling Patterns" - mentioned 6 times, no note
```

**Changes files:** No - read-only

---

### vault-stale

Find important notes that haven't been updated recently.

**You say:**
> "What important notes are stale?"
> "Find neglected documentation"
> "Which hub notes need updating?"
> "Show me outdated important notes"
> "What should I review?"

**Claude does:**
- Finds notes with high backlink counts
- Filters by last modification date
- Returns important but neglected notes

**You get:**

```
⏰ Stale Important Notes
- tech/frameworks/React.md (hub: 47 links, last updated 8 months ago)
- projects/legacy-api.md (12 links, last updated 1 year ago)
```

**Changes files:** No - read-only

---

### vault-dead-ends

Find notes others link to but that link nowhere themselves.

**You say:**
> "Find dead end notes"
> "Which notes don't link out?"
> "Show me notes that should have more links"
> "Find notes with only incoming links"
> "What notes are dead ends?"

**Claude does:**
- Finds notes with backlinks but zero forward links
- These often need expansion or linking

**You get:**

```
🛑 Dead End Notes
- concepts/microservices.md (8 backlinks, 0 outgoing)
- tech/tools/webpack.md (5 backlinks, 0 outgoing)
```

**Changes files:** No - read-only

---

## Link Analysis

All link analysis skills are **read-only**.

**Requires:** [smoking-mirror MCP](installation/mcp-servers.md)

### vault-backlinks

Show all notes linking to a specific note.

**You say:**
> "What links to my React note?"
> "Show backlinks for Project Alpha"
> "Who references this note?"
> "What notes mention Claude Code?"
> "Find everything linking to API Design"

**Claude does:**
- Queries smoking-mirror for backlinks
- Returns list with link context

**You get:**

```
🔗 Backlinks to React.md (47 found)
- projects/dashboard.md: "Built with [[React]] and TypeScript"
- tech/frontend/state-management.md: "[[React]] Context API..."
- daily-notes/2026-01-01.md: "Learning [[React]] hooks"
...
```

**Changes files:** No - read-only

---

### vault-related

Find notes similar to a specific note based on shared links and tags.

**You say:**
> "What's related to my React note?"
> "Find similar notes to Project Alpha"
> "What notes are like this one?"
> "Show me related content"
> "Find notes connected to API Design"

**Claude does:**
- Analyzes shared links, tags, and references
- Scores similarity based on overlap
- Returns ranked list

**You get:**

```
📎 Related to React.md
1. tech/frontend/Vue.md (similarity: 0.85) - shared: JavaScript, Frontend, Components
2. tech/frontend/Angular.md (similarity: 0.72) - shared: Frontend, TypeScript
3. projects/dashboard.md (similarity: 0.68) - shared: React, TypeScript
```

**Changes files:** No - read-only

---

### vault-path

Find the shortest connection path between two notes.

**User Story**: As a knowledge worker, I want to see how two concepts connect, so I can understand their relationship.

**You say:**
> "How does React connect to my Project Alpha note?"
> "Find the path from API Design to Security"
> "What's the link chain between these notes?"
> "How are these two concepts connected?"
> "Show me the relationship path"

**Claude does:**
- Queries smoking-mirror for shortest path
- Returns link chain with intermediate notes

**You get:**

```
🛤️ Path: React.md → Project Alpha.md
React.md → tech/frontend/state-management.md → projects/dashboard.md → Project Alpha.md
(3 hops)
```

**Changes files:** No - read-only

---

### vault-strength

Get a connection strength score between two notes.

**You say:**
> "How strongly connected are React and Project Alpha?"
> "What's the relationship strength between these notes?"
> "Rate the connection between API Design and Security"
> "How related are these two?"
> "Connection strength check"

**Claude does:**
- Analyzes multiple relationship factors
- Calculates composite strength score (0-100)
- Breaks down scoring factors

**You get:**

```
💪 Connection Strength: React.md ↔ Project Alpha.md
Score: 78/100 (Strong)

Breakdown:
- Direct link: Yes (+30)
- Shared neighbors: 5 (+25)
- Common tags: 3 (+15)
- Path length: 1 hop (+8)
```

**Changes files:** No - read-only

---

### vault-common

Find notes that two notes both reference (shared context).

**You say:**
> "What do React and Vue have in common?"
> "Find shared references between these notes"
> "What notes do both of these link to?"
> "Common neighbors between A and B"
> "Shared context between these topics"

**Claude does:**
- Queries forward links from both notes
- Finds intersection
- Returns shared references

**You get:**

```
🤝 Common Neighbors: React.md & Vue.md
- tech/frontend/components.md
- concepts/virtual-dom.md
- tech/frontend/state-management.md
```

**Changes files:** No - read-only

---

### vault-bidirectional

Find all mutual links in your vault (A ↔ B relationships).

**You say:**
> "Find bidirectional links"
> "What notes link to each other?"
> "Show me mutual relationships"
> "Find two-way links"
> "Which notes have reciprocal links?"

**Claude does:**
- Scans all links in vault
- Identifies pairs where both notes link to each other
- These indicate strong relationships

**You get:**

```
↔️ Bidirectional Links (23 pairs)
- React.md ↔ JavaScript.md
- Project Alpha.md ↔ API Design.md
- Database.md ↔ PostgreSQL.md
...
```

**Changes files:** No - read-only

---

### vault-link-density

Analyze link patterns across your vault.

**You say:**
> "Analyze my link density"
> "How well connected is my vault?"
> "Show me link patterns"
> "What's my linking behavior like?"
> "Link analysis report"

**Claude does:**
- Calculates links per note distribution
- Identifies over/under-linked areas
- Provides recommendations

**You get:**

```
📊 Link Density Analysis
Average: 2.89 links/note
Median: 2 links/note
Distribution:
- 0 links: 43 notes (1.5%)
- 1-3 links: 1,847 notes (65%)
- 4-10 links: 892 notes (31%)
- 10+ links: 65 notes (2.3%)

📝 Recommendations:
- 43 orphan notes could use connections
- tech/ folder has lower density (1.2 avg)
```

**Changes files:** No - read-only

---

### vault-unlinked-mentions

Find text mentions of a term not yet converted to wikilinks.

**You say:**
> "Find unlinked mentions of React"
> "Where is 'API design' mentioned but not linked?"
> "Show me linking opportunities for this term"
> "What plain text mentions should be wikilinks?"
> "Find text that should be linked"

**Claude does:**
- Searches for plain text mentions of term
- Excludes existing wikilinks
- Returns locations with context

**You get:**

```
🔍 Unlinked mentions of "React" (12 found)
- daily-notes/2026-01-01.md: "...working on React components..."
- projects/notes.md: "...the React ecosystem has..."
- tech/overview.md: "...frameworks like React and Vue..."
```

**Changes files:** No - read-only

---

### vault-suggest

Get wikilink suggestions for a specific note.

**You say:**
> "Suggest links for this note"
> "What should I link in my React note?"
> "Find linking opportunities"
> "What wikilinks am I missing?"
> "Improve links in this note"

**Claude does:**
- Analyzes note content
- Matches against known entities in vault
- Suggests wikilinks to add

**You get:**

```
💡 Suggested Links for project-notes.md
- "JavaScript" → [[JavaScript]]
- "API endpoint" → [[API Design]]
- "database query" → [[PostgreSQL]]
```

**Changes files:** No - read-only

---

## Structure Analysis

**Requires:** [smoking-mirror MCP](installation/mcp-servers.md)

### vault-section

Extract content from a specific heading without reading the whole file.

**You say:**
> "Show me the Log section from today's note"
> "Get the Tasks section from my daily note"
> "What's under the Setup heading in the README?"
> "Extract the Installation section"
> "Show me just the Goals section"

**Claude does:**
- Queries smoking-mirror for section content
- Returns just that heading's content
- Saves tokens by not reading whole file

**You get:**

```markdown
## Log (from daily-notes/2026-01-01.md)
- 09:15 Fixed authentication bug
- 14:30 Deployed v2.1
- 16:00 Meeting with team
```

**Changes files:** No - read-only

---

### vault-find-sections

Find all headings matching a pattern across your vault.

**You say:**
> "Find all ## Tasks sections"
> "Where do I have Setup headings?"
> "Find all notes with a Goals section"
> "Show me Installation sections across my vault"
> "What notes have a Log heading?"

**Claude does:**
- Searches all markdown files for matching headings
- Returns file paths with heading locations

**You get:**

```
📑 Found "## Tasks" in 47 files:
- daily-notes/2026-01-01.md (line 15)
- daily-notes/2025-12-31.md (line 18)
- projects/alpha/todo.md (line 3)
...
```

**Changes files:** No - read-only

---

### vault-folder-health

Check folder organization and recommendations.

**You say:**
> "How's my folder structure?"
> "Analyze my vault organization"
> "Check folder health"
> "Is my vault well organized?"
> "Folder structure analysis"

**Claude does:**
- Analyzes folder hierarchy
- Checks for files in wrong locations
- Identifies organizational issues

**You get:**

```
📁 Folder Health Report
✅ daily-notes/: Well organized (365 files)
✅ tech/: Good structure (5 subfolders)
⚠️ projects/: 12 files at root level (should be in subfolders)
❌ personal/: Files at root (violates hierarchy rules)
```

**Changes files:** No - read-only

---

### vault-clusters

Detect topic clusters from link patterns.

**You say:**
> "What topic clusters exist in my vault?"
> "Find related note groups"
> "Show me knowledge clusters"
> "How does my vault naturally group?"
> "Detect communities in my notes"

**Claude does:**
- Analyzes link graph structure
- Identifies densely-connected clusters
- Names clusters based on common tags/content

**You get:**

```
🔮 Topic Clusters Detected
1. Frontend Development (34 notes)
   Core: React.md, Vue.md, JavaScript.md
2. Project Alpha (28 notes)
   Core: Project Alpha.md, API Design.md, Database.md
3. Personal Goals (15 notes)
   Core: Goals 2026.md, Health.md, Career.md
```

**Changes files:** No - read-only

---

## Frontmatter Intelligence

**Requires:** [smoking-mirror MCP](installation/mcp-servers.md)

### vault-schema

See all YAML frontmatter fields used across your vault.

**You say:**
> "What frontmatter fields do I use?"
> "Show me my YAML schema"
> "What metadata fields exist in my vault?"
> "List all frontmatter keys"
> "Frontmatter overview"

**Claude does:**
- Scans all frontmatter across vault
- Compiles unique field names
- Shows usage counts

**You get:**

```
📋 Frontmatter Schema
- tags: 2,341 notes
- created: 1,892 notes
- status: 456 notes
- priority: 234 notes
- project: 178 notes
```

**Changes files:** No - read-only

---

### vault-schema-check

Find type inconsistencies in frontmatter (string vs array, etc.).

**You say:**
> "Check my frontmatter for problems"
> "Find schema inconsistencies"
> "What frontmatter is broken?"
> "Audit my YAML fields"
> "Frontmatter type check"

**Claude does:**
- Analyzes field types across vault
- Identifies inconsistencies (string vs array, number vs string)
- Reports problematic files

**You get:**

```
⚠️ Schema Inconsistencies Found
'tags' field:
- 2,329 notes: array (correct)
- 12 notes: string (inconsistent)
  - projects/old-note.md: tags: "work"
  - daily-notes/2024-01-01.md: tags: "journal"

'priority' field:
- 230 notes: number
- 4 notes: string ("high" instead of 1)
```

**Changes files:** No - read-only

---

### vault-field-values

Get all unique values for a specific frontmatter field.

**You say:**
> "What values does the 'status' field have?"
> "Show me all tag values"
> "What priorities are used?"
> "List all project values"
> "What are my status options?"

**Claude does:**
- Queries specific field across vault
- Returns unique values with counts

**You get:**

```
📊 Values for 'status' field
- draft: 145 notes
- published: 234 notes
- archived: 67 notes
- review: 23 notes
```

**Changes files:** No - read-only

---

## Task Management

**Requires:** [smoking-mirror MCP](installation/mcp-servers.md)

### vault-tasks

Get all tasks across your vault with filtering.

**You say:**
> "Show me all my tasks"
> "What tasks do I have?"
> "List incomplete tasks"
> "Find tasks in the projects folder"
> "Show me tasks tagged with work"

**Claude does:**
- Scans all markdown for task syntax
- Filters by status, folder, tag as requested
- Returns organized list

**You get:**

```
✅ Tasks (127 total, 89 incomplete)

## Incomplete
- [ ] Review PR #123 📅 2026-01-02 (daily-notes/2026-01-01.md)
- [ ] Finish quarterly report 📅 2026-01-15 (projects/q1.md)
- [ ] Update documentation (tech/docs/todo.md)

## Completed (last 7 days)
- [x] Deploy v2.1 (daily-notes/2025-12-31.md)
- [x] Fix auth bug (daily-notes/2025-12-30.md)
```

**Changes files:** No - read-only

---

### vault-due

Get tasks with due dates, sorted by deadline.

**You say:**
> "What tasks are due soon?"
> "Show me upcoming deadlines"
> "What's due this week?"
> "Task deadlines"
> "Overdue tasks?"

**Claude does:**
- Finds tasks with 📅 date markers
- Sorts by due date
- Highlights overdue items

**You get:**

```
📅 Tasks by Due Date
OVERDUE:
- [ ] Review PR #123 📅 2025-12-30 ⚠️

THIS WEEK:
- [ ] Finish quarterly report 📅 2026-01-03
- [ ] Call client 📅 2026-01-05

LATER:
- [ ] Annual review 📅 2026-01-15
```

**Changes files:** No - read-only

---

## Activity Tracking

### vault-activity

See recent modification patterns and trends.

**You say:**
> "What's my recent vault activity?"
> "Show me modification trends"
> "When was I most active?"
> "Vault activity report"
> "What have I been working on?"

**Claude does:**
- Analyzes file modification timestamps
- Groups by day/week
- Identifies patterns

**You get:**

```
📈 Vault Activity (last 30 days)
Most active: Mondays (avg 12 notes)
Least active: Weekends (avg 3 notes)

This week: 34 notes modified
Last week: 28 notes modified

Hot folders:
- daily-notes/: 30 changes
- projects/alpha/: 15 changes
- tech/: 8 changes
```

**Changes files:** No - read-only

---

### vault-concurrent

Find notes edited around the same time as a specific note.

**You say:**
> "What was I working on when I wrote this note?"
> "Find notes from the same session"
> "What else did I edit that day?"
> "Concurrent edits to this note"
> "Related work from that time"

**Claude does:**
- Gets target note's modification time
- Finds notes modified within ±2 hours
- Returns contextually related edits

**You get:**

```
⏰ Notes edited around React.md (2026-01-01 14:30)
Within 2 hours:
- tech/frontend/state-management.md (14:15)
- projects/dashboard.md (14:45)
- daily-notes/2026-01-01.md (15:00)
```

**Changes files:** No - read-only

---

## Link Maintenance

### vault-fix-links

Find and repair broken wikilinks.

**You say:**
> "Fix my broken links"
> "Repair dead wikilinks"
> "Find and fix broken references"
> "Clean up my links"
> "What links are broken?"

**Claude does:**
- Scans for wikilinks pointing to non-existent notes
- Suggests fixes (rename, create, remove)
- Applies fixes with your confirmation

**You get:**

```
🔧 Broken Links Found (7)
- [[Old Project Name]] → [[Project Alpha]]? (renamed)
- [[Typo Note]] → create new note?
- [[Deleted Thing]] → remove link?

Fix these? (y/n for each)
```

**Changes files:** Yes - with confirmation

---

### vault-search

Advanced search with frontmatter, tags, and folder filters.

**You say:**
> "Search for notes in tech folder with work tag"
> "Find status:draft notes"
> "Search for project:alpha notes"
> "Find notes tagged important in projects folder"
> "Advanced search: folder tech, tag typescript"

**Claude does:**
- Queries smoking-mirror with filters
- Combines multiple criteria
- Returns matching notes

**You get:**

```
🔍 Search Results
Filters: folder=tech, tags=work

Found 23 notes:
- tech/frameworks/React.md
- tech/tools/webpack.md
- tech/patterns/api-design.md
...
```

**Changes files:** No - read-only

---

## Wikilink Automation

### rebuild-wikilink-cache

Rebuild the entity cache from your vault content.

**You say:**
> "Rebuild the wikilink cache"
> "Refresh entity cache"
> "Update the link suggestions database"
> "Rebuild link cache"
> "Rescan for entities"

**Claude does:**
- Scans all note titles and aliases
- Builds entity recognition cache
- Prepares for auto-linking

**You get:**

```
🔄 Wikilink Cache Rebuilt
Entities indexed: 2,847
Aliases indexed: 456
Ready for auto-linking
```

**Changes files:** Yes - updates cache file

---

### wikilink-apply

Apply wikilink suggestions to a specific note.

**You say:**
> "Add wikilinks to this note"
> "Apply link suggestions to project-notes.md"
> "Convert plain text to wikilinks"
> "Auto-link this note"
> "Wikify this document"

**Claude does:**
- Analyzes note content
- Finds plain text matching known entities
- Converts to [[wikilinks]]

**Before:**

```markdown
Working on the React project with TypeScript.
Need to update the API design document.
```

**After:**

```markdown
Working on the [[React]] project with [[TypeScript]].
Need to update the [[API Design]] document.
```

**Changes files:** Yes - edits specified note

---

## Periodic Rollups

### rollup

Execute the complete rollup chain for the last 2 months.

**You say:**
> "Run the full rollup"
> "Create all my summary notes"
> "Roll up my daily notes"
> "Generate periodic summaries"
> "Execute rollup chain"

**Claude does:**
1. Daily → Weekly (last 8 weeks)
2. Weekly → Monthly (last 2 months)
3. Monthly → Quarterly (current quarter)
4. Quarterly → Yearly (current year)

**You get:**
- `weekly-notes/2026-W01.md` created
- `monthly-notes/2026-01.md` created
- `quarterly-notes/2026-Q1.md` updated
- `yearly-notes/2026.md` updated

**Changes files:** Yes - creates/updates rollup notes

---

### rollup-weekly

Summarize a specific week from daily notes.

**You say:**
> "Create a weekly summary for this week"
> "Roll up week 1 of 2026"
> "Summarize last week"
> "Generate weekly rollup for 2026-W01"
> "Weekly summary please"

**Claude does:**
- Reads daily notes for that week
- Extracts key themes, achievements, tasks
- Creates structured weekly summary

**Creates:** `weekly-notes/2026-W01.md`

**Changes files:** Yes - creates weekly note

---

### rollup-monthly

Summarize a specific month from weekly notes.

**You say:**
> "Create a monthly summary for January"
> "Roll up this month"
> "Summarize January 2026"
> "Generate monthly rollup"
> "Monthly summary please"

**Claude does:**
- Reads weekly notes for that month
- Synthesizes themes and progress
- Creates structured monthly summary

**Creates:** `monthly-notes/2026-01.md`

**Changes files:** Yes - creates monthly note

---

### rollup-quarterly

Summarize a specific quarter from monthly notes.

**You say:**
> "Create a Q1 summary"
> "Roll up this quarter"
> "Summarize Q1 2026"
> "Generate quarterly rollup"
> "Quarterly summary please"

**Claude does:**
- Reads monthly notes for that quarter
- Identifies quarter-level themes and achievements
- Creates structured quarterly summary

**Creates:** `quarterly-notes/2026-Q1.md`

**Changes files:** Yes - creates quarterly note

---

### rollup-yearly

Summarize a specific year from quarterly notes.

**You say:**
> "Create a 2026 yearly summary"
> "Roll up the year"
> "Annual summary please"
> "Generate yearly rollup"
> "Year in review"

**Claude does:**
- Reads quarterly notes for that year
- Synthesizes year-level narrative
- Creates structured yearly summary

**Creates:** `yearly-notes/2026.md`

**Changes files:** Yes - creates yearly note

---

## Hooks (Automatic)

Hooks run automatically - no commands needed. They trigger on specific events.

### session-start

**Triggers:** When Claude Code starts in your vault

**Shows:**
- Daily note status
- Habit progress (if tracking habits)
- Wikilink cache count
- Recent achievements

**You see:**

```
👋 Good morning!
📅 Daily note: 2026-01-01.md exists
✅ Habits: 3/5 complete
🔗 Wikilink cache: 2,847 entities
🏆 Recent: "Deployed v2.1" (yesterday)
```

---

### achievement-detect

**Triggers:** After editing daily notes

**Detects 126 patterns** including:
- Actions: built, created, deployed, fixed, shipped
- Progress: completed, finished, launched
- Success: works, passed, all tests green
- Milestones: v1.0, first time, breakthrough
- Bold text: `**Anything in bold**`
- Emojis: ✅ 🎉 🚀 💪 🏆

**Auto-adds to:** `Achievements.md`

---

### wikilink-suggest

**Triggers:** After Edit/Write operations

Auto-applies `[[wikilinks]]` to known entities in your notes using the entity cache.

---

### syntax-validate

**Triggers:** After Edit/Write operations

**Warns about:**
- Wrapped wikilinks (`**[[Link]]**`) - breaks links
- Angle brackets (`ILogger<T>`) - breaks all links after
- Wikilinks in frontmatter - corrupts YAML

---

## Intelligent Agents (8 Agents)

Agents are autonomous workflows. Just describe what you want - Claude picks the right agent.

### Rollup Agents (5)

| Agent | Source | Creates |
|-------|--------|---------|
| Daily Rollup | Today's daily note | Highlights summary |
| Weekly Rollup | Daily notes | `weekly-notes/YYYY-WNN.md` |
| Monthly Rollup | Weekly notes | `monthly-notes/YYYY-MM.md` |
| Quarterly Rollup | Monthly notes | `quarterly-notes/YYYY-QN.md` |
| Yearly Rollup | Quarterly notes | `yearly-notes/YYYY.md` |

### Analysis Agents (3)

| Agent | Purpose | Changes Files? |
|-------|---------|----------------|
| **Achievement Extractor** | Finds wins in your logs (126 patterns) | Yes - updates Achievements.md |
| **Schema Enforcer** | Audits frontmatter, fixes inconsistencies | With confirmation |
| **Relationship Explorer** | Deep relationship analysis between notes | No - read-only |

**Example conversation:**

```
You: "How do my project notes relate to my tech notes?"
Claude: [Invokes relationship-explorer agent]
        [Returns comprehensive relationship report]

You: "My frontmatter is a mess. Can you audit it?"
Claude: [Invokes schema-enforcer agent]
        [Returns schema report with fix suggestions]
```

---

## Configuration

All paths configured in `.obsidian-scribe.json`:

```json
{
  "paths": {
    "daily_notes": "daily-notes",
    "weekly_notes": "weekly-notes",
    "monthly_notes": "monthly-notes",
    "quarterly_notes": "quarterly-notes",
    "yearly_notes": "yearly-notes",
    "achievements": "personal/goals/Achievements.md",
    "templates": "templates"
  },
  "sections": {
    "log": "## Log",
    "tasks": "## Tasks",
    "food": "# Food"
  }
}
```

---

## Dependencies

| Feature | Requires |
|---------|----------|
| All hooks | Python 3.8+ |
| 16 vault-* skills | smoking-mirror MCP |
| wikilink-apply | smoking-mirror MCP |
| Other skills | None (works out of box) |

---

## Related

- [Use Cases](use-cases.md) - User stories with tool invocations and JSON output
- [Workflows](workflows.md) - End-to-end workflow examples
- [MCP Setup](installation/mcp-servers.md) - Enable vault intelligence
