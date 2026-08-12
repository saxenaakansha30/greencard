# Greencard

A personal issue tracker that runs entirely from the command line. No server, no database, no dependencies — just Python and JSON files.

## Requirements

Python 3.9+

## Usage

### Projects

```bash
# Add a project
python main.py project add <id> <name> --desc "optional description"
python main.py project add gc "Greencard"

# List projects
python main.py project list
```

### Issues

```bash
# Add an issue
python main.py add <title> --project <id> --priority <low|medium|high> --desc "..." --tags tag1 tag2
python main.py add "Fix login bug" --project gc --priority high --tags bug auth

# List issues (all filters optional)
python main.py list
python main.py list --project gc
python main.py list --status in_progress
python main.py list --priority high

# Show full details of an issue
python main.py show <id>

# Update an issue
python main.py update <id> --status <todo|in_progress|done>
python main.py update <id> --priority high --title "New title"

# Delete an issue
python main.py delete <id>
```

### Search

Searches across title, description, and tags.

```bash
python main.py search "login"
```

## Data

Issues and projects are stored as JSON files in the `data/` directory, created automatically on first use.

```
data/
  issues.json
  projects.json
```
