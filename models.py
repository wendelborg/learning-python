from dataclasses import dataclass


@dataclass
class Task:
    title: str
    done: bool = False

    def __str__(self) -> str:
        status = "[x]" if self.done else "[ ]"
        return f"{status} {self.title}"

    def mark_done(self) -> None:
        self.done = True
