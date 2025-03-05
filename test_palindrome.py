"""
Tests the palindrome module
"""
import pytest
from palindrome import *

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
    assert is_palindrome("") == False
def test_is_palindrome_single_char():
    assert is_palindrome("a") is True
    assert is_palindrome("bb") is True # commit #8 - test passed, no changes to code
    assert is_palindrome("abc") is False #commit #10 - test passed, no changes to code
    assert is_palindrome("laval") is True # commit #12 - test passed, no changes to code
    assert is_palindrome("toronto") is False #commit #14 - test passed, no changes to code
    assert is_palindrome("Able was I ere I saw Elba") is True #commit #15 test failed // commit #16 test passed
def test_palindrome_result():
    assert palindrome_result("abba") == "abba is a palindrome"
    assert palindrome_result("ccdd") == "ccdd is NOT a palindrome"
