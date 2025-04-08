from lib.gratitudes import *

def test_initial_gratitudes_list():
    grati = Gratitudes()
    result = grati.format()
    assert result == "Be grateful for: "

def test_adding_1_gratitude():
    grati = Gratitudes()
    grati.add("your family")
    result = grati.format()
    assert result == "Be grateful for: your family"

def test_adding_2_gratitudes():
    grati = Gratitudes()
    grati.add("your family")
    grati.add("your friends")
    result = grati.format()
    assert result == "Be grateful for: your family, your friends"

def test_adding_3_plus_gratitudes():
    grati = Gratitudes()
    grati.add("your pets")
    grati.add("the food on your table")
    grati.add("the love in your home")
    grati.add("the code in your life!")
    result = grati.format()
    assert result == "Be grateful for: your pets, the food on your table, the love in your home, the code in your life!"


