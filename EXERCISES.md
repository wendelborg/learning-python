# Exercises

---

## Step 1: Basic Syntax

### 1.1 — Task counter
**Status:** Done

Add a variable to count how many tasks have been added this session. Print the count after each add.

### 1.2 — Quit confirmation
**Status:** Done

When the user picks "Quit", ask "Are you sure? (y/n)" and only exit if they type "y".

---

## Step 2: Lists, Dicts, and Type Conversion

### 2.1 — Store tasks in a list of dicts
**Status:** Done

Create an empty `tasks` list. When adding a task, append a dict with `"title"` and `"done"` keys.

### 2.2 — Display tasks with numbering
**Status:** Done

Loop through tasks with `enumerate` and print each with its number and done status (`[ ]` / `[x]`).

### 2.3 — Mark task as done
**Status:** Done

Add a menu option to mark a task as done. Prompt for the task number and update the dict.

---

## Step 3: Functions

### 3.1 — Extract `add_task(tasks)`
**Status:** Done

Move the add logic into its own function.

### 3.2 — Extract `list_tasks(tasks)`
**Status:** Done

Move the list logic into its own function. Handle the empty list case.

### 3.3 — Extract `mark_task_done(tasks)`
**Status:** Done

Move the mark-done logic into its own function.

---

## Step 4: Classes

### 4.1 — Create a `Task` class
**Status:** Done

Create a class with `__init__(self, title)` and `__str__(self)`.

### 4.2 — Add `mark_done(self)` method
**Status:** Done

Add a method on the class to mark the task as done.

### 4.3 — Refactor functions to use `Task` objects
**Status:** Done

Replace dict access (`task["title"]`) with attribute access (`task.title`).

### 4.4 (Bonus) — Use a ternary expression in `__str__`
**Status:** Done

---

## Step 5: File I/O, JSON, Context Managers

### 5.1 — Write `save_tasks()` method
**Status:** Done

Convert Task objects to dicts using `__dict__` and write as JSON to `tasks.json`.

### 5.2 — Write `load_tasks()` method
**Status:** Done

Read `tasks.json` if it exists, parse JSON, and rebuild `Task` objects from dicts.

### 5.3 — Auto-save after mutations
**Status:** Done

Call `save_tasks()` after every add or mark-done.

### 5.4 — Auto-load at startup
**Status:** Done

Load from `tasks.json` in the `Tasks` constructor if the file exists.

---

## Step 6: List Comprehensions and Generators

### 6.1 — Basic comprehension
**Status:** Done

Double all numbers in a list. (`step6_comprehensions.py`)

### 6.2 — Filtered comprehension
**Status:** Done

Filter a list to only even numbers. (`step6_comprehensions.py`)

### 6.3 — Transform + filter
**Status:** Done

Double values, but only for numbers > 5. (`step6_comprehensions.py`)

### 6.4 — Strings
**Status:** Done

Uppercase names shorter than 5 characters. (`step6_comprehensions.py`)

### 6.5 — Counting with sum()
**Status:** Done

Count items matching a condition using `sum()` with a generator. (`step6_comprehensions.py`)

### 6.6 — Apply to task tracker
**Status:** Done

Add `summary()` and "list remaining" to `Tasks` class in `main.py`.

---

## Step 7: Type Hints and Dataclasses

### 7.1 — Convert `Task` to a dataclass
**Status:** Done

Replace manual `__init__` with `@dataclass` decorator. Keep `__str__` and `mark_done`.

### 7.2 — Add type hints to all functions
**Status:** Done

Add parameter types and return types (`-> None`, `-> str`, etc.) to all functions and methods.

### 7.3 — Use `asdict()` for serialization
**Status:** Done

Replace `task.__dict__` with `asdict(task)` in `save_tasks`.

### 7.4 — Use `**dict` unpacking for deserialization
**Status:** Done

Replace manual Task construction with `Task(**item)` in `load_tasks`.

### 7.5 — Pass mypy with no errors
**Status:** Done

Fix all type errors reported by `mypy main.py`.

---

## Step 8: Error Handling

### 8.1 — Validate numeric input
**Status:** Done

Created `get_int_input()` helper that loops until the user enters a valid number. Catches `ValueError`.

### 8.2 — Handle bounds in mark_task_done
**Status:** Done

Bounds check in `Tasks.mark_task_done` prevents invalid task numbers.

### 8.3 — Handle corrupted JSON
**Status:** Done

Catch `json.JSONDecodeError` in `load_tasks`, fall back to empty list.

### 8.4 — Add missing type hints and pass mypy
**Status:** Done

Added return types to all methods including `Iterator[Task]` for `__iter__`.
