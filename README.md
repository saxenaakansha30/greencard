# Greencard

A personal issue tracker that runs entirely from the command line. No server, no database, no dependencies — just Python and JSON files.

## Requirements

Python 3.9+

## Install

```bash
git clone <this-repo>
cd greencard
python3 -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -e .
```

This puts both `greencard` and its short form `gc` on your `PATH` inside
the virtual environment (via pip's console-script mechanism) — no shell
aliases or system-wide PATH edits needed. Data is still stored next to the
source in `data/`, regardless of which directory you run the command from.

`list` also has a short alias, `ls` (e.g. `gc ls`, `gc project ls`).

Since `greencard` only lives inside the venv, `activate` it in any new
shell session before using the command:

```bash
cd greencard
source .venv/bin/activate
gc list
```

## Usage

### Projects

```bash
# Add a project
gc project add <id> <name> --desc "optional description"
gc project add app "My App"

# List projects (alias: ls)
gc project list
gc project ls

# Update a project
gc project update <id> --name "New Name" --desc "New description"
gc project update app --name "My App v2"

# Delete a project (blocked while issues still reference it)
gc project delete <id>
gc project delete app
```

### Issues

```bash
# Add an issue
gc add <title> --project <id> --priority <low|medium|high> --desc "..." --tags tag1 tag2
gc add "Fix login bug" --project app --priority high --tags bug auth

# List issues (all filters optional; alias: ls)
gc list
gc ls --project app
gc list --status in_progress
gc list --priority high
gc list --limit 5

# Show full details of an issue
gc show <id>

# Update an issue
gc update <id> --status <todo|in_progress|done>
gc update <id> --priority high --title "New title"

# Delete an issue
gc delete <id>
```

### Search

Searches across title, description, and tags.

```bash
gc search "login"
```

## Data

Issues and projects are stored as JSON files in the `data/` directory, created automatically on first use.

```
data/
  issues.json
  projects.json
```
