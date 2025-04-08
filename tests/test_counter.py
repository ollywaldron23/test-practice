from lib.counter import *

def test_counter_with_no_adds():
    count1 = Counter()
    result = count1.report()
    assert result == "Counted to 0 so far."


def test_counter_adding_one_number():
    count1 = Counter()
    count1.add(5)
    result = count1.report()
    assert result == "Counted to 5 so far."

def test_counter_adding_2_numbers():
    count1 = Counter()
    count1.add(5)
    count1.add(45)
    result = count1.report()
    assert result == "Counted to 50 so far."

def test_counter_adding_and_taking_away():
    count1 = Counter()
    count1.add(50)
    count1.add(-26)
    result = count1.report()
    assert result == "Counted to 24 so far."

