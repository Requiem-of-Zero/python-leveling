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
