# Python Learning Notes

A C# developer's guide to Python — concepts learned while building a task tracker CLI.

---

## Step 1: Basic Syntax

### Indentation is syntax
Python uses a colon `:` and indented blocks instead of braces `{}`.

```csharp
// C#
if (choice == "1")
{
    Console.WriteLine("Hello");
}
```

```python
# Python
if choice == "1":
    print("Hello")
```

### No semicolons, no type declarations
Variables are dynamically typed — no `string`, `int`, or even `var` needed.

```csharp
// C#
string name = "Alice";
var age = 30;
```

```python
# Python
name = "Alice"
age = 30
```

### String interpolation
f-strings work like C# interpolated strings.

```csharp
// C#
Console.WriteLine($"Hello, {name}!");
```

```python
# Python
print(f"Hello, {name}!")
```

### User input

```csharp
// C#
string input = Console.ReadLine();
```

```python
# Python — input() always returns a string
name = input("Prompt: ")
```

### Control flow
`if / elif / else` instead of `if / else if / else`. No parentheses required around conditions.

```python
if choice == "1":
    print("one")
elif choice == "2":
    print("two")
else:
    print("other")
```

### Loops
`while True:` with `break` works the same as C#, minus the braces.

```python
while True:
    choice = input("Pick: ")
    if choice == "quit":
        break
```

### Entry point
Python doesn't have a `static void Main()`. Instead, use this pattern:

```python
if __name__ == "__main__":
    main()
```

This ensures the code runs only when the file is executed directly, not when imported as a module.

---

## Step 2: Lists, Dicts, and Type Conversion

### Lists (like `List<T>`)
```csharp
// C#
var tasks = new List<string>();
tasks.Add("Buy milk");
tasks.Count;
```

```python
# Python
tasks = []
tasks.append("Buy milk")
len(tasks)
```

### Dicts (like `Dictionary<K,V>` or anonymous objects)
```csharp
// C#
var task = new Dictionary<string, object> { {"title", "Buy milk"}, {"done", false} };
task["title"];
```

```python
# Python
task = {"title": "Buy milk", "done": False}
task["title"]
task["done"] = True
```

Note: Booleans are `True` / `False` (capitalized), not `true` / `false`.

### Looping with index — `enumerate`
```csharp
// C#
for (int i = 0; i < tasks.Count; i++) { ... }
// or with LINQ: tasks.Select((t, i) => ...)
```

```python
# Python
for i, task in enumerate(tasks):
    print(f"{i + 1}. {task['title']}")
```

### Type conversion (not casting)
Python doesn't cast with `(int)x`. Instead, call the type as a function:

```csharp
// C#
int num = int.Parse(Console.ReadLine());
```

```python
# Python
num = int(input("Enter number: "))    # string → int
pi = float("3.14")                     # string → float
label = str(42)                        # int → string
```

Invalid input raises `ValueError` (like C#'s `FormatException`).

### Conventions
- Python uses `snake_case` for variables and functions, not `camelCase`
- This is defined in PEP 8, Python's official style guide

---

## Step 3: Functions

### Defining functions
```csharp
// C#
public void Greet(string name, string greeting = "Hello") { ... }
```

```python
# Python — no access modifiers, no type declarations
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
```

### Keyword arguments
```python
greet(greeting="Hi", name="Bob")  # call by name, any order
```

### Returning multiple values
```csharp
// C# — need Tuple or out params
public (int total, int done) GetStats() { ... }
```

```python
# Python — just return a tuple, unpack at the call site
def get_stats(tasks):
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    return total, done

total, done = get_stats(tasks)
```

### Truthiness
Empty collections are "falsy" — no need for `.Count == 0` or `.Any()`.

```python
if not tasks:       # True when list is empty
    print("No tasks yet.")
    return          # early return, like C# void methods
```

Falsy values: `False`, `None`, `0`, `""`, `[]`, `{}`, `()`

### No hoisting
Functions must be defined before they're *called at runtime*. Order of definition doesn't matter if the call happens later:

```python
def main():
    greet("Alice")   # OK — greet exists by the time main() runs

def greet(name):
    print(f"Hello, {name}!")

main()               # both functions defined by now
```

### Functions without return
Functions without `return` return `None` (similar to void → null).

---

## Step 4: Classes

### Defining a class
```csharp
// C#
public class Task
{
    public string Title { get; set; }
    public bool Done { get; set; }
    public Task(string title) { Title = title; Done = false; }
    public override string ToString() => $"[{(Done ? "x" : " ")}] {Title}";
}
```

```python
# Python
class Task:
    def __init__(self, title):    # constructor (__init__, not __init)
        self.title = title         # no field declarations — just assign on self
        self.done = False

    def __str__(self):            # ToString()
        status = "[x]" if self.done else "[ ]"
        return f"{status} {self.title}"

    def mark_done(self):
        self.done = True
```

### Key differences from C#
- **`self` is explicit** — first parameter on every instance method, used to access fields. Like `this` but you must write it out.
- **`__init__`** = constructor. Called "dunder init" (double underscore).
- **`__str__`** = `ToString()`. Called automatically by `print()` and f-strings.
- **No access modifiers** — everything is public. Prefix with `_` for "private by convention".
- **No property/field declarations** — assign `self.whatever` in `__init__`.

### Ternary expressions
```csharp
// C#
var status = done ? "[x]" : "[ ]";
```

```python
# Python — value_if_true if condition else value_if_false
status = "[x]" if self.done else "[ ]"
```

### __str__ and f-strings
When you put an object in an f-string, Python calls `__str__` automatically:

```python
task = Task("Buy milk")
print(f"1. {task}")      # calls task.__str__() → "1. [ ] Buy milk"
```

---

## Step 5: File I/O, JSON, and Context Managers

### Imports
```python
import json      # built-in JSON module
import os        # file system operations
```

### JSON serialization
```csharp
// C#
var json = JsonSerializer.Serialize(tasks);
var tasks = JsonSerializer.Deserialize<List<Task>>(json);
```

```python
# Python — json module works with dicts/lists, not custom classes
text = json.dumps(data, indent=2)    # serialize (dict/list → string)
data = json.loads(text)               # deserialize (string → dict/list)
```

Python's `json` module can't auto-serialize custom classes. Options:
- `task.__dict__` — every object has this, returns its attributes as a dict
- `dataclasses.asdict()` — cleaner, covered in Step 7

### File I/O with `with` (like `using`)
```csharp
// C#
using (var writer = new StreamWriter("tasks.json"))
    writer.Write(json);
```

```python
# Python — 'with' ensures the file is closed, like 'using' in C#
with open("tasks.json", "w") as f:    # "w" = write, "r" = read
    f.write(text)

with open("tasks.json", "r") as f:
    text = f.read()
```

### Checking file existence
```python
import os
if os.path.exists("tasks.json"):
    ...
```

### `__iter__` — making a class iterable
```csharp
// C#
public class Tasks : IEnumerable<Task> { ... }
```

```python
# Python — implement __iter__ to support for-loops
class Tasks:
    def __iter__(self):
        return iter(self.tasks)
```

### List comprehensions (preview — Step 6)
```csharp
// C#
var data = tasks.Select(t => t.ToDict()).ToList();
```

```python
# Python — list comprehension
data = [task.__dict__ for task in self.tasks]
```

---

## Step 6: List Comprehensions and Generators

### Basic pattern
```
[expression for item in collection]
[expression for item in collection if condition]
```

Read as: "give me `expression` for each `item` in `collection` (if `condition`)".

### Comparison with LINQ
```csharp
// C# — chain left to right
tasks.Where(t => t.Done).Select(t => t.Title).ToList();
```

```python
# Python — expression first, then loop, then filter
[t.title for t in tasks if t.done]
```

### Comprehension with enumerate (preserving index)
```python
# Keep original index while filtering — produces list of (index, item) tuples
not_done = [(i, task) for i, task in enumerate(self.tasks) if not task.done]
for i, task in not_done:
    print(f"{i + 1}. {task}")
```

### Counting with sum() + generator
```csharp
// C#
tasks.Count(t => t.Done);
```

```python
# Python — generator expression (round parens = lazy)
done = sum(1 for t in tasks if t.done)
```

### List vs generator
- `[...]` = list — built in memory immediately (like `.ToList()`)
- `(...)` = generator — lazy, one value at a time (like `IEnumerable`)

---

## Step 7: Type Hints and Dataclasses

### Type hints
Optional annotations — not enforced at runtime, but checked by tools like `mypy`.

```csharp
// C#
public string Greet(string name, int times = 1) { ... }
```

```python
# Python
def greet(name: str, times: int = 1) -> str:
    ...

# void → None
def mark_done(self) -> None:
    self.done = True

# Collections
tasks: list[Task] = []
data: dict[str, bool] = {"done": True}
```

### Dataclasses (like C# records)
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

Auto-generates `__init__`, `__repr__`, and `__eq__`. You can still add methods.

### `asdict()` — clean serialization
Replaces `task.__dict__` for dataclasses:

```python
from dataclasses import asdict
data = asdict(task)    # {"title": "Buy milk", "done": False}
```

### `**dict` unpacking — clean deserialization
```python
d = {"title": "Buy milk", "done": True}
task = Task(**d)    # same as Task(title="Buy milk", done=True)
```

### `__post_init__` — extra constructor logic
```python
@dataclass
class Task:
    title: str
    done: bool = False

    def __post_init__(self) -> None:
        self.title = self.title.strip()
```

### Linting and type checking
```bash
pip3 install mypy ruff
mypy main.py          # type checker
ruff check main.py    # linter
ruff format main.py   # auto-formatter
```

---

## Step 8: Error Handling

### try/except (like try/catch)
```csharp
// C#
try { int n = int.Parse(input); }
catch (FormatException e) { ... }
catch (Exception e) { ... }
finally { ... }
```

```python
# Python
try:
    n = int(input("Number: "))
except ValueError as e:       # FormatException equivalent
    print(f"Invalid: {e}")
except Exception as e:
    print(f"Error: {e}")
finally:
    ...
```

### Common exception mapping
| Python | C# |
|---|---|
| `ValueError` | `FormatException` |
| `IndexError` | `IndexOutOfRangeException` |
| `KeyError` | `KeyNotFoundException` |
| `FileNotFoundError` | `FileNotFoundException` |
| `TypeError` | `InvalidCastException` |
| `json.JSONDecodeError` | `JsonException` |

### Iterator type hints
```python
from collections.abc import Iterator

# Like IEnumerator<Task> in C#
def __iter__(self) -> Iterator[Task]:
    return iter(self.tasks)
```

---

## Progress

- [x] Step 1 — Basic syntax, variables, f-strings, control flow
- [x] Step 2 — Lists, dicts, type conversion, snake_case
- [x] Step 3 — Functions, truthiness, early return
- [x] Step 4 — Classes, __init__, __str__, ternary
- [x] Step 5 — File I/O, JSON, context managers, __iter__
- [x] Step 6 — List comprehensions, generators
- [x] Step 7 — Type hints, dataclasses, mypy, ruff
- [x] Step 8 — Error handling, try/except, exception types
- [ ] Step 9 — Modules & packages
- [ ] Step 10 — Virtual environments, pip
