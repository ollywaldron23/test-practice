from lib.todo import *
import pytest

#Given task is blank and complete is set to false, check complete is false():
def test_no_task_complete_false_returns_complete_false():
    todo = Todo("")
    assert todo.complete == False

#Given task and complete set to false, check complete false():

def test_add_task_returns_complete_false():
    todo = Todo("Walk the dog")
    assert todo.complete == False

#Given task and complete set to false, call mark complete and check complete true():
def test_add_task_calling_mark_complete_returns_complete_true():
    todo = Todo("Walk the dog")
    todo.mark_complete()
    assert todo.complete == True

#Given a non string input for task, return exception
def test_non_string_inputted_for_task_returns_error():
    with pytest.raises(TypeError) as e:
        Todo(451)
    assert str(e.value) == "Task must be a string"
    
