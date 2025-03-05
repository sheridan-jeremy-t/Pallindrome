"""
Validates strings as palindromes.
"""
from collections import deque

def main():
    raise NotImplemented
if __name__ == '__main__':
    main()

def is_palindrome(text: str)-> bool:
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    if not text:
        return False