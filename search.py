import display
import storage


def search(query: str):
    query = query.lower()
    results = [
        i for i in storage.load_issues()
        if query in i.title.lower()
        or query in i.description.lower()
        or any(query in tag.lower() for tag in i.tags)
    ]
    display.print_issues(results)
