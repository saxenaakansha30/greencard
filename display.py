from models import Issue, Project

_PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def print_issues(issues: list[Issue]):
    if not issues:
        print("No issues found.")
        return
    issues = sorted(issues, key=lambda i: (_PRIORITY_ORDER.get(i.priority, 1), i.id))
    print(f"{'ID':<5} {'PROJECT':<12} {'STATUS':<15} {'PRIORITY':<10} TITLE")
    print("-" * 70)
    for i in issues:
        print(f"{i.id:<5} {i.project:<12} {i.status:<15} {i.priority:<10} {i.title}")


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
