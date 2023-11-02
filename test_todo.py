import datetime

import pytest
import todo


@pytest.fixture
def my_task():
    return todo.Task(
        'A task',
        datetime.date(2023, 11, 3)
    )


@pytest.fixture
def another_task():
    return todo.Task(
        'Another task',
        datetime.date(2023, 11, 5)
    )


def test_set_priority(my_task):
    my_task.set_priority(5)
    assert my_task.priority == 5


def test_mark_done(my_task):
    my_task.mark_done()
    assert my_task.complete is True


@pytest.fixture
def my_list(my_task, another_task):
    my_list = todo.ToDoList()
    my_list.add_task(my_task)
    return my_list


def test_add_task(my_list, another_task):
    my_list.add_task(another_task)
    assert another_task in my_list.todo_list


def test_del_task(my_list, my_task):
    my_list.del_task(my_task)
    assert my_task not in my_list.todo_list

