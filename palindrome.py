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

    text_deque = deque(text)
    while len(text_deque) > 1:
        if text_deque.popleft() != text_deque.pop():
            return False
    return True