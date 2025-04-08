import pytest
from lib.present import *

def test_no_contents():
    prezzie = Present()
    with pytest.raises(Exception) as e:
        prezzie.unwrap()
    result = str(e.value)
    assert result == "No contents have been wrapped."

def test_add_1_content():
    prezzie = Present()
    prezzie.wrap("gift 1")
    result = prezzie.unwrap()
    assert result == "gift 1"

def test_add_2_contents():
    prezzie = Present()
    prezzie.wrap("bike")
    with pytest.raises(Exception) as e:
        prezzie.wrap("toys")
    result = str(e.value)
    assert result == "A contents has already been wrapped."

def test_add_2_contents_wrap_value():
    prezzie = Present()
    prezzie.wrap("bike")
    with pytest.raises(Exception) as e:
        prezzie.wrap("toys")
    assert prezzie.unwrap() == "bike"

