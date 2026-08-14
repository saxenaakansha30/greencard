from models import Issue, Project

_PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}

_RESET = "\033[0m"
_RED = "\033[31m"
_BLUE = "\033[34m"
_GREEN = "\033[32m"

_STATUS_COLORS = {
    "done": _GREEN,
    "in_progress": _BLUE,
    "todo": _RED,
}

_PRIORITY_COLORS = {
    "high": _RED,
    "medium": _BLUE,
    "low": _GREEN,
}


def _colorize(text: str, color: str) -> str:
    return f"{color}{text}{_RESET}"


def _padded_colorize(text: str, width: int, color: str) -> str:
    return _colorize(text, color) + " " * (width - len(text))


def print_issues(issues: list[Issue], limit: int = None):
    if not issues:
        print("No issues found.")
        return
    issues = sorted(issues, key=lambda i: (_PRIORITY_ORDER.get(i.priority, 1), i.id))
    if limit:
        issues = issues[:limit]
    print(f"{'ID':<5} {'PROJECT':<12} {'STATUS':<15} {'PRIORITY':<10} TITLE")
    print("-" * 70)
    for i in issues:
        status = _padded_colorize(i.status, 15, _STATUS_COLORS.get(i.status, ""))
        priority = _padded_colorize(i.priority, 10, _PRIORITY_COLORS.get(i.priority, ""))
        print(f"{i.id:<5} {i.project:<12} {status} {priority} {i.title}")


def print_issue(issue: Issue):
    print(f"ID:          {issue.id}")
    print(f"Title:       {issue.title}")
    print(f"Project:     {issue.project}")
    print(f"Status:      {issue.status}")
    print(f"Priority:    {issue.priority}")
    if issue.description:
        print(f"Description: {issue.description}")
    if issue.tags:
        print(f"Tags:        {', '.join(issue.tags)}")
    print(f"Created:     {issue.created_at}")
    print(f"Updated:     {issue.updated_at}")


def print_projects(projects: list[Project]):
    if not projects:
        print("No projects found.")
        return
    print(f"{'ID':<12} {'NAME':<20} DESCRIPTION")
    print("-" * 50)
    for p in projects:
        print(f"{p.id:<12} {p.name:<20} {p.description}")
