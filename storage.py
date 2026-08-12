import json
from pathlib import Path

from models import Issue, Project

DATA_DIR = Path(__file__).parent / "data"
ISSUES_FILE = DATA_DIR / "issues.json"
PROJECTS_FILE = DATA_DIR / "projects.json"


def _ensure_data_dir():
    DATA_DIR.mkdir(exist_ok=True)


def load_issues() -> list[Issue]:
    if not ISSUES_FILE.exists():
        return []
    with open(ISSUES_FILE) as f:
        return [Issue(**i) for i in json.load(f)]


def save_issues(issues: list[Issue]):
    _ensure_data_dir()
    with open(ISSUES_FILE, "w") as f:
        json.dump([vars(i) for i in issues], f, indent=2)


def load_projects() -> list[Project]:
    if not PROJECTS_FILE.exists():
        return []
    with open(PROJECTS_FILE) as f:
        return [Project(**p) for p in json.load(f)]


def save_projects(projects: list[Project]):
    _ensure_data_dir()
    with open(PROJECTS_FILE, "w") as f:
        json.dump([vars(p) for p in projects], f, indent=2)


def next_issue_id(issues: list[Issue]) -> int:
    return max((i.id for i in issues), default=0) + 1
