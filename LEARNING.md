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

## Progress

- [x] Step 1 — Basic syntax, variables, f-strings, control flow
- [x] Step 2 — Lists, dicts, type conversion, snake_case
- [ ] Step 3 — Functions, default args, *args/**kwargs
- [ ] Step 4 — Classes, __init__, __str__
- [ ] Step 5 — File I/O, JSON, context managers
- [ ] Step 6 — List comprehensions, generators
- [ ] Step 7 — Type hints, dataclasses
- [ ] Step 8 — Error handling, custom exceptions
- [ ] Step 9 — Modules & packages
- [ ] Step 10 — Virtual environments, pip
