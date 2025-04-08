import pytest
from lib.password_checker import *
def test_long_enough_password():
    password = PasswordChecker()
    password.check("ilovecode")
    assert True

def test_too_short_password():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("icode")
    result = str(e.value)
    assert result == "Invalid password, must be 8+ characters."

def test_exactly_8_character_password():
    password = PasswordChecker()
    password.check("lovecode")
    assert True

def test_empty_string():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("")
    result = str(e.value)
    assert result == "Invalid password, must be 8+ characters."

def test_long_password():
    password = PasswordChecker()
    password.check("ilovelovelovelovecode")
    assert True
