import os  # Module for interacting with the operating system (file operations)
import pytest  # pytest testing framework

# Import all CRUD functions to test from your module
from todo_crud import (
    load_tasks,
    save_tasks,
    add_task,
    get_task,
    list_tasks,
    complete_task,
    edit_task,
    remove_task
)

# Autouse fixture: runs before and after every test automatically
@pytest.fixture(autouse=True)
def clean_data_file():
    """
    Ensure a clean test environment by deleting the JSON data file
    both before and after each test runs.
    """
    # SETUP PHASE: before the test
    if os.path.exists("todo.json"):
        os.remove("todo.json")  # remove leftover file
    yield  # run the test now
    # TEARDOWN PHASE: after the test
    if os.path.exists("todo.json"):
        os.remove("todo.json")  # clean up again


def test_load_save_empty():
    """
    Test behavior of load_tasks() on empty storage and
test save_tasks()/load_tasks() round-trip.
    """
    # Initially, no data file exists → load_tasks returns empty list
    assert load_tasks() == []

    # Create a sample list and save it
    sample = [{"id": 1, "title": "Task", "completed": False}]
    save_tasks(sample)

    # After saving, load_tasks should return the same list
    assert load_tasks() == sample


def test_add_and_get_task():
    """
    Test add_task() behavior and retrieval via get_task().
    """
    # Add a new task with a due date
    t = add_task("Test", "05/31/2025")

    # The returned dict should have the expected fields
    assert t["id"] == 1
    assert t["title"] == "Test"
    # due should be converted to ISO format starting with the expected date
    assert t["due"].startswith("2025-05-31T")

    # get_task(1) should return the exact same dict
    g = get_task(1)
    assert g == t


def test_list_tasks_flags():
    """
    Test list_tasks() filtering logic with show_all flag.
    """
    # Add two tasks
    add_task("A")
    add_task("B")

    # By default, both are incomplete → list_tasks returns 2 items
    assert len(list_tasks()) == 2

    # Complete the first task
    complete_task(1)

    # Now only one incomplete remains
    assert len(list_tasks()) == 1

    # With show_all=True, both should be listed again
    assert len(list_tasks(show_all=True)) == 2


def test_complete_task():
    """
    Test complete_task() idempotency and return values.
    """
    # Add a task and complete it
    add_task("X")
    assert complete_task(1) is True  # first completion returns True

    # Trying to complete again should return False
    assert complete_task(1) is False


def test_edit_task():
    """
    Test editing title and due date, and invalid due date error.
    """
    # Add a task with initial due date
    add_task("Old", "01/01/2025")

    # Edit both title and due date
    assert edit_task(1, title="New", due="12/31/2025")
    t = get_task(1)
    assert t["title"] == "New"
    assert t["due"].startswith("2025-12-31T")

    # Passing a bad due-date format should raise a ValueError
    with pytest.raises(ValueError):
        edit_task(1, due="bad-date")


def test_remove_task():
    """
    Test remove_task() successful deletion and handling of non-existent ID.
    """
    # Add two tasks
    add_task("Z")
    add_task("Y")

    # Remove the first task → returns True, and it should no longer exist
    assert remove_task(1) is True
    assert get_task(1) is None

    # Only one task remains
    assert len(list_tasks(show_all=True)) == 1

    # Removing a non-existent ID should return False
    assert remove_task(99) is False
