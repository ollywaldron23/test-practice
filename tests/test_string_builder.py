from lib.string_builder import *

def test_return_initial_string():
    string = StringBuilder()
    result = string.output()
    assert result == ""

def test_add_1_item_to_string():
    string = StringBuilder()
    string.add("Hello")
    result = string.output()
    assert result == "Hello"

def test_add_two_items_to_string():
    string = StringBuilder()
    string.add("Hello! ")
    string.add("How are you doing?")
    result = string.output()
    assert result == "Hello! How are you doing?"

def test_return_length_of_string():
    string = StringBuilder()
    string.add("Hello there, I love to code.")
    result = string.size()
    assert result == 28


