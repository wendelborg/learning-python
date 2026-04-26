# Task Tracker - A Python learning project
# Step 1: Basic syntax, variables, f-strings, control flow
#
# Key differences from C#:
# - No braces {} for blocks — indentation matters (4 spaces by convention)
# - No semicolons
# - No explicit types (dynamically typed)
# - print() instead of Console.WriteLine()
# - input() instead of Console.ReadLine()
# - f"..." instead of $"..." for string interpolation

class Task:
    def __init__(self, title):
        self.title = title
        self.done = False
    
    def __str__(self):
        status = "[x]" if self.done else "[ ]"
        return f"{status} {self.title}"
    
    def mark_done(self):
        self.done = True

def add_task(tasks):
    description = input("Enter task description: ")
    task = Task(description)
    tasks.append(task) 

def list_tasks(tasks):
    if not tasks:
        print("No tasks added yet.")
        return
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")

def mark_task_done(tasks):
    task_num = input("Enter task number to mark as done: ")
    task = tasks[int(task_num) - 1]
    task.mark_done()

def main():
    print("=== Task Tracker ===")
    print()

    # Variables - no type declaration needed (like 'var' everywhere, but truly dynamic)
    name = input("What's your name? ")

    # f-strings work like C# interpolated strings ($"Hello {name}")
    print(f"\nWelcome, {name}!")
    print()

    # A counter for number of tasks added
    tasks = []  # This will hold our tasks (we'll use it in a future step)

    # A simple loop - note the colon and indentation instead of braces
    # In C#: while (true) { ... }
    while True:
        print("What would you like to do?")
        print("  1. Add a task")
        print("  2. List tasks")
        print("  3. Mark task as done") 
        print("  4. Quit") 
        print()

        choice = input("Enter your choice (1-4): ")

        # No switch statement needed (Python 3.10+ has 'match', but if/elif is idiomatic)
        # In C#: if (choice == "1") { } else if (choice == "2") { }
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            sure = input("Are you sure? (y/n): ")
            if sure.lower() == "y":                
                print(f"Goodbye, {name}!")
                break  # same as C#
        else:
            print("  Invalid choice, try again.")

        print()


# This is Python's equivalent of C#'s static void Main()
# The __name__ check ensures this only runs when executed directly,
# not when imported as a module (similar to how a class library
# vs console app works)
if __name__ == "__main__":
    main()
