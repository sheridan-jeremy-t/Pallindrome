"""
Validates strings as palindromes.
"""
from collections import deque

def is_palindrome(text: str)-> bool:
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    if not text:
        return False
    cleaned_text = text.lower().strip() #convert input text to all lower case and remove all white space
    text_deque = deque(cleaned_text)
    while len(text_deque) > 1:
        if text_deque.popleft() != text_deque.pop():
            return False
    return True
def main():
    user_input = input("What would you like to check? ")
    is_palindrome(user_input)

if __name__ == '__main__':
    main()