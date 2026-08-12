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
