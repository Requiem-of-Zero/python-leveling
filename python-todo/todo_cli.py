import argparse
from todo_crud import add_task, list_tasks, get_task, complete_task, edit_task, remove_task

def main():
  parser = argparse.ArgumentParser(
    prog='python-todo',
    description='Simple CLI to-do CRUD logic'
  )

  sub = parser.add_subparsers(
    dest="command",
    required=True
  )

  parser_add = sub.add_parser(
    "add",
    help="Add a new task"
  )

  parser_add.add_argument(
    "title",
    help="Task title"
  )

  parser_add.add_argument(
    "--due",
    help="Due date in MM/DD/YYYY format",
    default=None
  )

  parser_list = sub.add_parser(
    "list",
    help="List tasks"
  )

  parser_list.add_argument(
    "--all",
    action="store_true",
    help="Show all tasks, including the completed ones"
  )

  parser_get = sub.add_parser(
    "get",
    help="Show details of a task"
  )

  parser_get.add_argument(
    "id",
    type=int,
    help="ID of the task you are trying to get"
  )

  parser_done = sub.add_parser(
    "done",
    help="Mark task as done"
  )

  parser_done.add_argument(
    "id",
    type=int,
    help="ID of the task you are trying to complete"
  )

  parser_edit = sub.add_parser(
    "edit",
    help="Edit a task"
  )

  parser_edit.add_argument(
    "id",
    type=int,
    help="ID of the task you are trying to edit"
  )

  parser_edit.add_argument(
    "--title",
    help="New title for the task"
  )

  parser_edit.add_argument(
    "--due",
    help="New due date for the task in MM/DD/YYYY format"
  )

  parser_remove = sub.add_parser(
    "rm",
    help="Remove a task"
  )

  parser_remove.add_argument(
    "id",
    type=int,
    help="ID of the task you are trying to remove"
  )

  args = parser.parse_args()

  if args.command == "add":
    task = add_task(args.title, args.due)
    print(f"Added task {task['id']}: {task['title']}")
  elif args.command == "list":
    tasks = list_tasks(show_all=args.all)
    for task in tasks:
      status = "✓" if task.get("completed") else "✗"  # check completion
      print(f"[{status}] {task['id']}: {task['title']} (due: {task.get('due')})")
  elif args.command == "get":
    task = get_task(args.id)
    if not task:
      print(f"No task found with ID: {args.id}")
    else:
      print(task)
  elif args.command == "done":
    ok = complete_task(args.id)
    print("Completed." if ok else f"Task {args.id} not found or already done.")
  elif args.command == "edit":
    ok = edit_task(args.id, title=args.title, due=args.due)
    print("Updated." if ok else f"Task {args.id} not found.")
  elif args.command == "rm":
    ok = remove_task(args.id)
    print("Removed." if ok else f"Task {args.id} not found")

if __name__ == "__main__":
  main()