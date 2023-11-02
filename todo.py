from dataclasses import dataclass
import datetime


# Let's create a class to store our tasks
# This feels like the simplest set up
# You can write the methods for yourself


class Task:
    def __init__(
            self,
            label: str,
            due_date: datetime.date,
            priority=0
    ):

        self.label = label
        self.due_date = due_date
        self.priority = priority
        self.complete: bool = False
        self.completed_date: datetime.date | None = None

# When a task is marked done we should also store the date
# The method for this is datetime.date.today()

    def mark_done(self):
        ...

# What should be returned when we want to print a task

    def __str__(self):
        ...

# Users should be able to set priorities

    def set_priority(self, priority: int):
        ...


# We need a way to store our tasks
# Initially this is just a fancy way of managing a list

class ToDoList:
    def __init__(self):
        self.todo_list = []

    # Just adding a task to our list

    def add_task(self, task: Task):
        ...

    # Just deleting a task from our list

    def del_task(self, task: Task):
        ...

    # Just setting the priority of a task

    def set_priority(self, task: Task, priority: int):
        ...

    # What do you want to see when we print the list?

    def __str__(self):
        ...

