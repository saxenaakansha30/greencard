import display
import storage
from models import Project


def add(project_id: str, name: str, description: str):
    projects = storage.load_projects()
    if any(p.id == project_id for p in projects):
        print(f"Project '{project_id}' already exists.")
        return
    projects.append(Project(id=project_id, name=name, description=description))
    storage.save_projects(projects)
    print(f"Created project '{project_id}': {name}")


def list_projects():
    display.print_projects(storage.load_projects())


def update(project_id: str, name: str, description: str):
    projects = storage.load_projects()
    project = next((p for p in projects if p.id == project_id), None)
    if not project:
        print(f"Project '{project_id}' not found.")
        return

    if name:
        project.name = name
    if description is not None:
        project.description = description

    storage.save_projects(projects)
    print(f"Updated project '{project_id}'")


def delete(project_id: str):
    projects = storage.load_projects()
    if not any(p.id == project_id for p in projects):
        print(f"Project '{project_id}' not found.")
        return

    issues = storage.load_issues()
    if any(i.project == project_id for i in issues):
        print(f"Cannot delete '{project_id}': issues still reference this project. Delete or reassign them first.")
        return

    updated = [p for p in projects if p.id != project_id]
    storage.save_projects(updated)
    print(f"Deleted project '{project_id}'")
