from collections.abc import Iterator
from dataclasses import asdict
from models import Task
import json
import os


class Tasks:
    def __init__(self) -> None:
        if os.path.exists("tasks.json"):
            self.load_tasks()
        else:
            self.tasks: list[Task] = []

    def add_task(self, title) -> None:
        task = Task(title)
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self) -> None:
        if not self.tasks:
            print("No tasks added yet.")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def mark_task_done(self, task_num) -> None:
        if 0 < task_num <= len(self.tasks):
            task = self.tasks[task_num - 1]
            task.mark_done()
            self.save_tasks()
        else:
            print("That is not a task number.")

    def __iter__(self) -> Iterator[Task]:
        return iter(self.tasks)

    def save_tasks(self) -> None:
        data = [asdict(task) for task in self.tasks]
        text = json.dumps(data, indent=2)
        with open("tasks.json", "w") as f:
            f.write(text)

    def load_tasks(self) -> None:
        try:
            with open("tasks.json", "r") as f:
                data = json.loads(f.read())
                self.tasks = [
                    Task(**item) for item in data
                ]  # Can be unpacked like this since Task is a dataclass
        except json.JSONDecodeError as e:
            print("Error loading tasks:", e)
            self.tasks = []

    def summary(self) -> None:
        total = len(self.tasks)
        done = sum(1 for task in self.tasks if task.done)
        print(f"Summary: {total} tasks ({done} done, {total - done} remaining)")

    def remaining(self) -> None:
        not_done = [(i, task) for i, task in enumerate(self.tasks) if not task.done]
        if not not_done:
            print("Clean sheets!")
            return
        for i, task in not_done:
            print(f"{i + 1}. {task}")
