import argparse

import issues
import projects
import search


def main():
    parser = argparse.ArgumentParser(prog="greencard")
    sub = parser.add_subparsers(dest="cmd")

    p_add = sub.add_parser("add", help="Add a new issue")
    p_add.add_argument("title")
    p_add.add_argument("--project", required=True)
    p_add.add_argument("--priority", default="medium", choices=["low", "medium", "high"])
    p_add.add_argument("--desc", default="")
    p_add.add_argument("--tags", nargs="*", default=[])

    p_list = sub.add_parser("list", help="List issues")
    p_list.add_argument("--project")
    p_list.add_argument("--status", choices=["todo", "in_progress", "done"])
    p_list.add_argument("--priority", choices=["low", "medium", "high"])

    p_update = sub.add_parser("update", help="Update an issue")
    p_update.add_argument("id", type=int)
    p_update.add_argument("--status", choices=["todo", "in_progress", "done"])
    p_update.add_argument("--priority", choices=["low", "medium", "high"])
    p_update.add_argument("--title")
    p_update.add_argument("--desc")

    p_delete = sub.add_parser("delete", help="Delete an issue")
    p_delete.add_argument("id", type=int)

    p_show = sub.add_parser("show", help="Show issue details")
    p_show.add_argument("id", type=int)

    p_search = sub.add_parser("search", help="Search issues")
    p_search.add_argument("query")

    p_project = sub.add_parser("project", help="Manage projects")
    proj_sub = p_project.add_subparsers(dest="proj_cmd")

    p_proj_add = proj_sub.add_parser("add", help="Add a project")
    p_proj_add.add_argument("id")
    p_proj_add.add_argument("name")
    p_proj_add.add_argument("--desc", default="")

    proj_sub.add_parser("list", help="List projects")

    args = parser.parse_args()

    if args.cmd == "add":
        issues.add(args.title, args.project, args.priority, args.desc, args.tags)
    elif args.cmd == "list":
        issues.list_issues(args.project, args.status, args.priority)
    elif args.cmd == "update":
        issues.update(args.id, args.status, args.priority, args.title, args.desc)
    elif args.cmd == "delete":
        issues.delete(args.id)
    elif args.cmd == "show":
        issues.show(args.id)
    elif args.cmd == "search":
        search.search(args.query)
    elif args.cmd == "project":
        if args.proj_cmd == "add":
            projects.add(args.id, args.name, args.desc)
        elif args.proj_cmd == "list":
            projects.list_projects()
        else:
            p_project.print_help()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
