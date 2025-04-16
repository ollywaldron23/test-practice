from lib.age_checker import *
import pytest

def test_sixteen_and_over_returns_access_granted():
    assert AgeChecker("1960-10-21") == "Access granted!"

def test_below_sixteen_returns_access_denied():
    assert AgeChecker("2011-04-15") == "Access denied!"

def test_raises_error_when_incorrect_date_format_entered():
    with pytest.raises(ValueError) as error:
        AgeChecker("15-04-2011")
    assert str(error.value) == "Date string is in the incorrect format!"

def test_raises_error_when_integer_is_entered():
    with pytest.raises(ValueError) as error:
        AgeChecker(55)
    assert str(error.value) == "Date string is in the incorrect format!"