# Python for C# Developers

A practical guide to Python — from the perspective of someone who's written C# for 20 years.

---

## Slide 1: Why This Talk?

Python is everywhere — data science, automation, AI/ML, scripting, web APIs.

If you know C#, you already know 80% of the concepts. This talk covers the 20% that's different.

We'll build a **task tracker CLI** from scratch, introducing one concept at a time.

---

## Slide 2: The Basics — What's Missing

No braces. No semicolons. No type declarations.

```csharp
// C#
if (choice == "1")
{
    Console.WriteLine($"Hello, {name}!");
}
```

```python
# Python
if choice == "1":
    print(f"Hello, {name}!")
```

- Indentation **is** syntax (4 spaces by convention)
- `elif` instead of `else if`
- No parentheses around conditions
- f-strings (`f"..."`) instead of interpolated strings (`$"..."`)

---

## Slide 3: Everything Is Dynamic

```csharp
// C#
string name = "Alice";
int age = 30;
List<string> items = new();
```

```python
# Python
name = "Alice"
age = 30
items = []
```

No `var`, no type declarations. Every variable is dynamically typed.

`input()` always returns a string — use `int()` / `float()` to convert (not cast).

---

## Slide 4: Collections

| C# | Python |
|---|---|
| `List<T>` | `list` — `[]` |
| `Dictionary<K,V>` | `dict` — `{}` |
| `(int, string)` tuple | `tuple` — `()` |
| `tasks.Add(x)` | `tasks.append(x)` |
| `tasks.Count` | `len(tasks)` |
| `true` / `false` | `True` / `False` |

```python
task = {"title": "Buy milk", "done": False}
task["done"] = True
```

---

## Slide 5: Functions

```csharp
// C#
public string Greet(string name, string greeting = "Hello") { ... }
```

```python
# Python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Call by name, any order
greet(greeting="Hi", name="Bob")

# Return multiple values — no Tuple<> needed
def get_stats(tasks):
    return len(tasks), sum(1 for t in tasks if t.done)

total, done = get_stats(tasks)
```

Functions without `return` return `None` (like void returning null).

---

## Slide 6: Truthiness

Empty collections are falsy. No need for `.Count == 0` or `.Any()`.

```python
if not tasks:           # True when list is empty
    print("No tasks.")
    return
```

Falsy values: `False`, `None`, `0`, `""`, `[]`, `{}`, `()`

Everything else is truthy.

---

## Slide 7: Classes

```csharp
// C#
public class Task
{
    public string Title { get; set; }
    public bool Done { get; set; }
    public Task(string title) { Title = title; }
    public override string ToString() => $"[{(Done ? "x" : " ")}] {Title}";
}
```

```python
# Python
class Task:
    def __init__(self, title):        # constructor
        self.title = title             # no field declarations
        self.done = False

    def __str__(self):                # ToString()
        status = "[x]" if self.done else "[ ]"
        return f"{status} {self.title}"
```

- **`self`** is explicit — like `this`, but you must write it everywhere
- **No access modifiers** — everything is public. `_prefix` = private by convention
- **No property declarations** — just assign on `self`

---

## Slide 8: Dataclasses — Python's Records

```csharp
// C#
public record Task(string Title, bool Done = false);
```

```python
from dataclasses import dataclass, asdict

@dataclass
class Task:
    title: str
    done: bool = False
```

Auto-generates `__init__`, `__repr__`, `__eq__`.

```python
asdict(task)          # → {"title": "Buy milk", "done": False}
Task(**some_dict)     # dict unpacking → Task(title=..., done=...)
```

---

## Slide 9: File I/O — `with` Is `using`

```csharp
// C#
using (var writer = new StreamWriter("data.json"))
    writer.Write(json);
```

```python
# Python
with open("data.json", "w") as f:
    f.write(json.dumps(data, indent=2))

with open("data.json", "r") as f:
    data = json.loads(f.read())
```

Python's `json` module works with dicts/lists, not custom classes. Convert first with `asdict()` or `__dict__`.

---

## Slide 10: List Comprehensions — Python's LINQ

This is where Python shines. One line replaces Select, Where, Count.

```csharp
// C# — chain left to right
tasks.Select(t => t.Title).ToList();
tasks.Where(t => t.Done).ToList();
tasks.Where(t => t.Done).Select(t => t.Title).ToList();
tasks.Count(t => t.Done);
```

```python
# Python — expression first, then loop, then filter
[t.title for t in tasks]
[t for t in tasks if t.done]
[t.title for t in tasks if t.done]
sum(1 for t in tasks if t.done)
```

`[...]` = list (eager, like `.ToList()`)
`(...)` = generator (lazy, like `IEnumerable`)

---

## Slide 11: Error Handling

```csharp
// C#
try { int n = int.Parse(input); }
catch (FormatException e) { ... }
finally { ... }
```

```python
# Python
try:
    n = int(user_input)
except ValueError as e:
    print(f"Invalid: {e}")
finally:
    ...
```

| Python | C# |
|---|---|
| `ValueError` | `FormatException` |
| `IndexError` | `IndexOutOfRangeException` |
| `KeyError` | `KeyNotFoundException` |
| `FileNotFoundError` | `FileNotFoundException` |

---

## Slide 12: Type Hints — Opt-in Static Typing

Not enforced at runtime. Checked by tools like `mypy`.

```python
def mark_done(self) -> None:           # void
    self.done = True

def get_stats(tasks: list[Task]) -> tuple[int, int]:
    ...

name: str | None = None                # string? (Python 3.10+)
```

```bash
mypy main.py     # type checker
ruff check .     # linter
ruff format .    # auto-formatter
```

---

## Slide 13: Modules — Files Are Namespaces

Every `.py` file is a module. No namespace declarations needed.

```
project/
├── main.py       # from models import Task
├── models.py     # Task dataclass
├── store.py      # persistence logic
└── utils.py      # helpers
```

```python
from models import Task          # like: using Models;
from store import Tasks          # like: using Store;
from utils import get_int_input  # like: using static Utils;
```

---

## Slide 14: Virtual Environments — Per-Project NuGet

```bash
python3 -m venv venv             # create (once)
source venv/bin/activate         # activate (per terminal)
pip install mypy ruff            # install packages
pip freeze > requirements.txt    # save deps (like .csproj)
pip install -r requirements.txt  # restore (like dotnet restore)
deactivate                       # back to system Python
```

Always `.gitignore` the `venv/` folder — like `bin/` and `obj/`.

---

## Slide 15: Convention Cheat Sheet

| Topic | C# | Python |
|---|---|---|
| Naming | `PascalCase` / `camelCase` | `snake_case` everywhere |
| Entry point | `static void Main()` | `if __name__ == "__main__":` |
| Null | `null` | `None` |
| Booleans | `true` / `false` | `True` / `False` |
| String interp | `$"Hello {x}"` | `f"Hello {x}"` |
| Blocks | `{ }` | `:` + indentation |
| Void return | `void` | `-> None` |
| Package manager | NuGet | pip |
| Style guide | .editorconfig | PEP 8 |

---

## Slide 16: What's Next?

- **Testing**: `pytest` — simpler than xUnit/NUnit
- **Web APIs**: FastAPI (modern, typed) or Flask (minimal)
- **Async**: `async` / `await` — same keywords, different runtime model
- **Decorators**: `@something` — like C# attributes, but they're functions
- **Package management**: `poetry` or `uv` — more modern than pip alone

---

## Resources

- [Python Docs](https://docs.python.org/3/)
- [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [Real Python](https://realpython.com/) — tutorials and guides
