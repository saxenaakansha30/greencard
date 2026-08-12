from dataclasses import dataclass, field


@dataclass
class Issue:
    id: int
    title: str
    project: str
    status: str = "todo"
    priority: str = "medium"
    description: str = ""
    tags: list[str] = field(default_factory=list)
    created_at: str = ""
    updated_at: str = ""


@dataclass
class Project:
    id: str
    name: str
    description: str = ""
