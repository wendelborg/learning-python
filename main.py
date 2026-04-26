import json
import os

from models import Task
from store import Tasks
from utils import get_int_input

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

def add_task(tasks: Tasks):
    description = input("Enter task description: ")
    tasks.add_task(description)
def list_tasks(tasks: Tasks):
    tasks.list_tasks()

def mark_task_done(tasks: Tasks):
    task_num = get_int_input("Enter task number to mark as done: ")
    tasks.mark_task_done(task_num)

def main():
    print("=== Task Tracker ===")
    print()

    # Variables - no type declaration needed (like 'var' everywhere, but truly dynamic)
    name = input("What's your name? ")

    # f-strings work like C# interpolated strings ($"Hello {name}")
    print(f"\nWelcome, {name}!")
    print()

    # A counter for number of tasks added
    tasks = Tasks()

    # A simple loop - note the colon and indentation instead of braces
    # In C#: while (true) { ... }
    while True:
        print("What would you like to do?")
        print("  1. Add a task")
        print("  2. List tasks")
        print("  3. Mark task as done") 
        print("  4. Summary") 
        print("  5. Remaining")         
        print("  6. Quit") 
        print()

        choice = input("Enter your choice (1-6): ")

        # No switch statement needed (Python 3.10+ has 'match', but if/elif is idiomatic)
        # In C#: if (choice == "1") { } else if (choice == "2") { }
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            tasks.summary()
        elif choice == "5":
            tasks.remaining()
        elif choice == "6":
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
