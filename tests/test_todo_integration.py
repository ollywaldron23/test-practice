from lib.todo import *
from lib.todo_list import *

#Add one incomplete todo and call incomplete, returns todo
def test_add_incomplete_todo_call_incomplete_return_todo():
    todolist = TodoList()
    todolist.add(Todo("Walk the dog"))
    result = todolist.incomplete()
    assert result == ["Walk the dog"]

#Add one complete todo and call incomplete, returns empty list
def test_add_complete_todo_call_incomplete_return_empty_list():
    todolist = TodoList()
    todo = Todo("Walk the dog")
    todo.mark_complete()
    todolist.add(todo)
    result = todolist.incomplete()
    assert result == []

#Add one complete todo and call complete, returns todo
def test_add_complete_todo_call_complete_return_todo():
    todolist = TodoList()
    todo = Todo("Walk the dog")
    todo.mark_complete()
    todolist.add(todo)
    result = todolist.complete()
    assert result == ["Walk the dog"]

#Add one complete and one incomplete task, call complete, returns one complete todo
def test_add_complete_and_incomplete_todo_call_complete_return_complete_todo():
    todolist = TodoList()
    todo = Todo("Walk the dog")
    todo1 = Todo("Cook dinner")
    todo.mark_complete()
    todolist.add(todo)
    todolist.add(todo1)
    result = todolist.complete()
    assert result == ["Walk the dog"]
    
#Add one complete and one incomplete task, call incomplete, returns one incomplete todo
def test_add_complete_and_incomplete_todo_call_incomplete_return_incomplete_todo():
    todolist = TodoList()
    todo = Todo("Walk the dog")
    todo1 = Todo("Cook dinner")
    todo.mark_complete()
    todolist.add(todo)
    todolist.add(todo1)
    result = todolist.incomplete()
    assert result == ["Cook dinner"]

#Add two incomplete todos, call give up, calling incomplete returns empty list
def test_add_two_incompletes_call_give_up_call_incomplete_returns_empty_list():
    todolist = TodoList()
    todo = Todo("Walk the dog")
    todo1 = Todo("Cook dinner")
    todolist.add(todo)
    todolist.add(todo1)
    todolist.give_up()
    result = todolist.incomplete()
    assert result == []

#Add two incomplete todos, call give up, calling complete returns both todos
def test_add_two_incompletes_call_give_up_call_complete_returns_todos():
    todolist = TodoList()
    todo = Todo("Walk the dog")
    todo1 = Todo("Cook dinner")
    todolist.add(todo)
    todolist.add(todo1)
    todolist.give_up()
    result = todolist.complete()
    assert result == ["Walk the dog", "Cook dinner"]

#Add one complete and one incomplete task, call give up, then complete, returns both todo
def test_add_complete_and_incomplete_todo_call_give_up_then_complete_returns_both_complete_todos():
    todolist = TodoList()
    todo = Todo("Walk the dog")
    todo1 = Todo("Cook dinner")
    todo.mark_complete()
    todolist.add(todo)
    todolist.add(todo1)
    todolist.give_up()
    result = todolist.complete()
    assert result == ["Walk the dog", "Cook dinner"]
