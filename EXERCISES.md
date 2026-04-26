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
**Status:** Pending

Create a class with `__init__(self, title)` and `__str__(self)`.

### 4.2 — Add `mark_done(self)` method
**Status:** Pending

Add a method on the class to mark the task as done.

### 4.3 — Refactor functions to use `Task` objects
**Status:** Pending

Replace dict access (`task["title"]`) with attribute access (`task.title`).

### 4.4 (Bonus) — Use a ternary expression in `__str__`
**Status:** Pending

Use `"x" if self.done else " "` instead of an if/else block.
