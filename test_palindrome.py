"""
Tests the palindrome module
"""
import pytest
from palindrome import is_palindrome, palindrome_result

def test_is_palindrome_string():
    """
    Test that is_palindrome raises a ValueError when given anything but a string

    :return: ValueError
    """
    with pytest.raises(ValueError):
        is_palindrome(123)
        is_palindrome(None)
        is_palindrome([])
def test_is_palindrome_string_empty():
    """
    Test if the string is empty
    :return: False if string is empty
    """
    assert is_palindrome("") is False
def test_is_palindrome():
    """
    Overall testing for the is_palindrome function
    :return: True if input is a palindrome, return False if not a palindrome
    """
    assert is_palindrome("a") is True
    assert is_palindrome("bb") is True # commit #8 - test passed, no changes to code
    assert is_palindrome("abc") is False #commit #10 - test passed, no changes to code
    assert is_palindrome("laval") is True # commit #12 - test passed, no changes to code
    assert is_palindrome("toronto") is False #commit #14 - test passed, no changes to code
    assert is_palindrome("Able was I ere I saw Elba") is True
def test_palindrome_result():
    """
    Testing output result
    :return: print statement confirming if input was a palindrome
    """
    assert palindrome_result("abba") == "abba is a palindrome"
    assert palindrome_result("ccdd") == "ccdd is NOT a palindrome"
