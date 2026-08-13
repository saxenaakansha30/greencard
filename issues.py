from datetime import datetime

import display
import storage
from models import Issue

VALID_STATUSES = {"todo", "in_progress", "done"}
VALID_PRIORITIES = {"low", "medium", "high"}


def _now() -> str:
    return datetime.now().isoformat(timespec="seconds")


def add(title: str, project_id: str, priority: str, description: str, tags: list[str]):
    if priority not in VALID_PRIORITIES:
        print(f"Invalid priority. Choose: {', '.join(sorted(VALID_PRIORITIES))}")
        return

    projects = storage.load_projects()
    if not any(p.id == project_id for p in projects):
        print(f"Project '{project_id}' not found. Create it first: greencard project add <id> <name>")
        return

    issues = storage.load_issues()
    issue = Issue(
        id=storage.next_issue_id(issues),
        title=title,
        project=project_id,
        priority=priority,
        description=description,
        tags=tags,
        created_at=_now(),
        updated_at=_now(),
    )
    issues.append(issue)
    storage.save_issues(issues)
    print(f"Created issue #{issue.id}: {issue.title}")


def list_issues(project: str, status: str, priority: str, limit: int = None):
    issues = storage.load_issues()
    if project:
        issues = [i for i in issues if i.project == project]
    if status:
        issues = [i for i in issues if i.status == status]
    if priority:
        issues = [i for i in issues if i.priority == priority]
    display.print_issues(issues, limit)


def update(issue_id: int, status: str, priority: str, title: str, description: str):
    issues = storage.load_issues()
    issue = next((i for i in issues if i.id == issue_id), None)
    if not issue:
        print(f"Issue #{issue_id} not found.")
        return

    if status:
        if status not in VALID_STATUSES:
            print(f"Invalid status. Choose: {', '.join(sorted(VALID_STATUSES))}")
            return
        issue.status = status
    if priority:
        if priority not in VALID_PRIORITIES:
            print(f"Invalid priority. Choose: {', '.join(sorted(VALID_PRIORITIES))}")
            return
        issue.priority = priority
    if title:
        issue.title = title
    if description is not None:
        issue.description = description

    issue.updated_at = _now()
    storage.save_issues(issues)
    print(f"Updated issue #{issue_id}")


def delete(issue_id: int):
    issues = storage.load_issues()
    updated = [i for i in issues if i.id != issue_id]
    if len(updated) == len(issues):
        print(f"Issue #{issue_id} not found.")
        return
    storage.save_issues(updated)
    print(f"Deleted issue #{issue_id}")


def show(issue_id: int):
    issues = storage.load_issues()
    issue = next((i for i in issues if i.id == issue_id), None)
    if not issue:
        print(f"Issue #{issue_id} not found.")
        return
    display.print_issue(issue)
