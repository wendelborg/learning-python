# Python Learning — A C# Developer's Journey

A hands-on Python learning project built from the perspective of a senior C# developer. Learn Python by building a task tracker CLI, one concept at a time.

## The Project

A command-line task tracker that supports adding, listing, completing, and persisting tasks to JSON. Built incrementally across 10 learning steps.

### Running

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

### Linting

```bash
source venv/bin/activate
bash lint.sh
```

## Repository Structure

### Application

| File | Description |
|---|---|
| `main.py` | Entry point — menu loop and user interaction |
| `models.py` | `Task` dataclass |
| `store.py` | `Tasks` class — collection management and JSON persistence |
| `utils.py` | Helper functions (`get_int_input`) |

### Learning Materials

| File | Description |
|---|---|
| `LEARNING.md` | Concept reference — side-by-side C# and Python comparisons for every topic covered |
| `EXERCISES.md` | All exercises with completion status |
| `PRESENTATION.md` | Slide deck — "Python for C# Developers" (16 slides, compatible with Marp/slides) |
| `step6_comprehensions.py` | Standalone exercise file for list comprehensions |

### Project Config

| File | Description |
|---|---|
| `requirements.txt` | Python dependencies (mypy, ruff) |
| `lint.sh` | Runs mypy and ruff |
| `.gitignore` | Excludes `venv/` |

## Topics Covered

1. Basic syntax, variables, f-strings, control flow
2. Lists, dicts, type conversion, snake_case
3. Functions, truthiness, early return
4. Classes, `__init__`, `__str__`, ternary expressions
5. File I/O, JSON, context managers, `__iter__`
6. List comprehensions, generators
7. Type hints, dataclasses, mypy, ruff
8. Error handling, try/except, exception types
9. Modules and packages
10. Virtual environments, pip, requirements.txt
