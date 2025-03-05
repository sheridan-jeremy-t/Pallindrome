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
    assert is_palindrome("bb") is True