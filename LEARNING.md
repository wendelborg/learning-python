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

## Progress

- [x] Step 1 — Basic syntax, variables, f-strings, control flow
- [ ] Step 2 — Lists, dicts, tuples
- [ ] Step 3 — Functions, default args, *args/**kwargs
- [ ] Step 4 — Classes, __init__, __str__
- [ ] Step 5 — File I/O, JSON, context managers
- [ ] Step 6 — List comprehensions, generators
- [ ] Step 7 — Type hints, dataclasses
- [ ] Step 8 — Error handling, custom exceptions
- [ ] Step 9 — Modules & packages
- [ ] Step 10 — Virtual environments, pip
