from dataclasses import dataclass, asdict
import json
import os

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

@dataclass
class Task:
    title: str
    done: bool = False
    
    def __str__(self):
        status = "[x]" if self.done else "[ ]"
        return f"{status} {self.title}"
    
    def mark_done(self):
        self.done = True

class Tasks:
    def __init__(self):
        if os.path.exists("tasks.json"):
            self.load_tasks()
        else:
            self.tasks: list[Task] = []
    
    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        self.save_tasks()
    
    def list_tasks(self):
        if not self.tasks:
            print("No tasks added yet.")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")
    
    def mark_task_done(self, task_num):
        if 0 < task_num <= len(self.tasks):
            task = self.tasks[task_num - 1]
            task.mark_done()
            self.save_tasks()  
        else:
            print("Invalid task number.")

    def __iter__(self):
        return iter(self.tasks)

    def save_tasks(self):
        data = [asdict(task) for task in self.tasks]
        text = json.dumps(data, indent = 2)
        with open("tasks.json", "w") as f:
            f.write(text)

    def load_tasks(self):
        with open("tasks.json", "r") as f:
            data = json.loads(f.read())
            self.tasks = [Task(**item) for item in data] # Can be unpacked like this since Task is a dataclass

    def summary(self): 
        total = len(self.tasks)
        done = sum(1 for task in self.tasks if task.done)
        print(f"Summary: {total} tasks ({done} done, {total - done} remaining)")

    def remaining(self):                                                                                                                                                                                                                        
        not_done = [(i, task) for i, task in enumerate(self.tasks) if not task.done]                                                                                                                                                            
        if not not_done:                                                                                                                                                                                                                        
            print("Clean sheets!")                                                                                                                                                                                                              
            return                                                                                                                                                                                                                              
        for i, task in not_done:                                     
            print(f"{i + 1}. {task}") 

def add_task(tasks: list[Task]):
    description = input("Enter task description: ")
    tasks.add_task(description)
def list_tasks(tasks: list[Task]):
    tasks.list_tasks()

def mark_task_done(tasks: list[Task]):
    task_num = input("Enter task number to mark as done: ")
    tasks.mark_task_done(int(task_num))

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
