from lib.most_often import *

#Given empty starting list returns no clear winner 

def test_empty_starting_list_no_clear_winner():
    mostoften = MostOften([])
    assert mostoften.get_most_often() == "no clear winner"

#Given a list of 1 integer, returns item

def test_given_one_integer_returns_same_integer():
    mostoften = MostOften([5])
    assert mostoften.get_most_often() == 5

#Given a list of 1 string, returns string

def test_given_one_string_returns_same_string():
    mostoften = MostOften(["Sunshine"])
    assert mostoften.get_most_often() == "Sunshine"

#Given a list of 6 integers, returns most common integer

def test_given_list_of_integers_returns_most_common():
    mostoften = MostOften([2, 1, 2, 5, 3, 2])
    assert mostoften.get_most_often() == 2

#Given a list of 6 integers, with 2 integers repeated the same number of times, returns "No clear winner"

def test_list_of_integers_with_no_clear_winner():
    mostoften = MostOften([2, 1, 2, 5, 3, 3])
    assert mostoften.get_most_often() == "no clear winner"

#Given a starting empty list, add one new item, returns that item as most common

def test_adding_new_item_to_empty_list_returns_same_item():
    mostoften = MostOften([])
    mostoften.add_new(1)
    assert mostoften.get_most_often() == 1

#Given a starting list of 5 items, adding one new item, returns most common

def test_add_new_item_to_starting_list_returns_most_common():
    mostoften = MostOften([2, 1, 2, 5, 3, 3])
    mostoften.add_new(2)
    assert mostoften.get_most_often() == 2

#Given a starting list of strings and integers, adding new string, returns that string as most common

def test_adding_string_to_list_of_strings_and_integers_returning_most_common_string():
    mostoften = MostOften([2, "Sunshine", 2, 5, 3, 3, "Sunshine"])
    mostoften.add_new("Sunshine")
    assert mostoften.get_most_often() == "Sunshine"

#Given a list of integers with a clear winner, add an integer to change the result to no clear winner.

def test_adding_an_integer_to_a_list_overiding_original_winner_returning_no_clear_winner():
    mostoften = MostOften([2, 1, 2, 5, 3, 3])
    mostoften.add_new(3)
    mostoften.add_new(2)
    assert mostoften.get_most_often() == "no clear winner"

