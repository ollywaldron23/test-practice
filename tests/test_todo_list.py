from lib.todo_list import *

#Given nothing has been added, calling incomplete will return an empty list
def test_no_task_calling_incomplete_returns_empty_list():
    todolist = TodoList()
    result = todolist.incomplete()
    assert result == []

#Given nothing has been added, calling complete will return an empty list
def test_no_task_calling_complete_returns_empty_list():
    todolist = TodoList()
    result = todolist.complete()
    assert result == []

def test_no_task_calling_give_up_then_complete_returns_empty_list():
    todolist = TodoList()
    todolist.give_up()
    result = todolist.complete()
    assert result == []


