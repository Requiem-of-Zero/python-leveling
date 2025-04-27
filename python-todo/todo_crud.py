import json  # JSON parsing and serialization
from pathlib import Path  # Filesystem path handling
from datetime import datetime  # for timestamps

DATA_FILE = Path("todo.json")

def load_tasks() -> list[dict]:
  if not DATA_FILE.exists():
    return []
  with DATA_FILE.open("r", encoding="utf-8") as todo_obj:
    data = json.load(todo_obj)
  return data.get("tasks", [])

def save_tasks(tasks: list[dict]) -> None:
  with DATA_FILE.open("w", encoding="utf-8") as todo_obj:
    json.dump({"tasks": tasks}, todo_obj, indent=2)

def add_task(title:str, due:str = None) -> dict:
  tasks = load_tasks()
  next_id = max((t.get("id", 0) for t in tasks), default=0) + 1

  try:
    due_dt = datetime.strptime(due, "%m/%d/%Y")
    due = due_dt.isoformat()
  except ValueError:
    raise ValueError(f"Invalid due date format: {due}. Use MM/DD/YYYY.")

  task = {
    "id": next_id,
    "title": title,
    "due": due,
    "completed": False,
    "created_at": datetime.now().isoformat()
  }
  
  tasks.append(task)
  save_tasks(tasks)
  return task

def list_tasks(show_all:bool = False) -> list[dict]:
  tasks = load_tasks()

  if show_all:
    return tasks

  filtered = []

  for task in tasks:
    completed_flag = task.get("completed")

    if not completed_flag:
      filtered.append(task)

  return filtered

def get_task(task_id: int) -> dict | None:
  tasks = load_tasks()
  
  for task in tasks:
    if task.get("id") == task_id:
      print(task)
  
  return None

def complete_task(task_id: int) -> bool:
  tasks = load_tasks()

  for task in tasks:
    if task.get("id") == task_id:
      if task.get("completed") == True:
        print("Already completed")
        return False
      task["completed"] = True
      task["completed_at"] = datetime.now().isoformat()
      save_tasks(tasks)
      return True

  return False

def edit_task(task_id: int, **fields) -> bool:
  tasks = load_tasks()

  for task in tasks:
    if task.get("id") == task_id:
      if 'title' in fields:
        task['title'] = fields['title']
      if 'due' in fields:
        due_val = fields['due']
        try:
          due_dt = datetime.strptime(due_val, "%m/%d/%Y")
          task['due'] = due_dt.isoformat()
        except ValueError:
          raise ValueError(f"Invalid due date format: {due_val}. Use MM/DD/YYYY.")
      save_tasks(tasks)
      print(tasks)
      return True

  print(tasks)
  return False