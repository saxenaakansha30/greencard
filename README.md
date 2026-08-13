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

This puts a `greencard` command on your `PATH` inside the virtual
environment (via pip's console-script mechanism) — no shell aliases or
system-wide PATH edits needed. Data is still stored next to the source in
`data/`, regardless of which directory you run `greencard` from.

Since `greencard` only lives inside the venv, `activate` it in any new
shell session before using the command:

```bash
cd greencard
source .venv/bin/activate
greencard list
```

## Usage

### Projects

```bash
# Add a project
greencard project add <id> <name> --desc "optional description"
greencard project add gc "Greencard"

# List projects
greencard project list
```

### Issues

```bash
# Add an issue
greencard add <title> --project <id> --priority <low|medium|high> --desc "..." --tags tag1 tag2
greencard add "Fix login bug" --project gc --priority high --tags bug auth

# List issues (all filters optional)
greencard list
greencard list --project gc
greencard list --status in_progress
greencard list --priority high

# Show full details of an issue
greencard show <id>

# Update an issue
greencard update <id> --status <todo|in_progress|done>
greencard update <id> --priority high --title "New title"

# Delete an issue
greencard delete <id>
```

### Search

Searches across title, description, and tags.

```bash
greencard search "login"
```

## Data

Issues and projects are stored as JSON files in the `data/` directory, created automatically on first use.

```
data/
  issues.json
  projects.json
```
