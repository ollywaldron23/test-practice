from lib.report_length import *
def test_report_length():
    assert report_length("six") == "This string was 3 characters long."
    assert report_length("pear") == "This string was 4 characters long."
    assert report_length("soo many") == "This string was 8 characters long."
