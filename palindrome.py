"""
Validates strings as palindromes.
"""
from collections import deque

def is_palindrome(text: str)-> bool:
    """
    Main function to check if input is a palindrome
    :param text: User Input must be a string
    :return: Will return a bool
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    if not text:
        return False
    cleaned_text = text.lower().strip()
    text_deque = deque(cleaned_text)
    while len(text_deque) > 1:
        if text_deque.popleft() != text_deque.pop():
            return False
    return True
def palindrome_result(text: str) -> str:
    """
    After checking in is_palindrome create a print statement
    :param text: User input MUST be a string
    :return: Return a usable f-string for printing to console
    """
    if is_palindrome(text):
        return f"{text} is a palindrome"
    return f"{text} is NOT a palindrome"
def main() -> None:
    """
    Main call function with variable user input
    :return: Returns palindrome_result to console
    """
    user_input: str = input("What would you like to check? ")
    confirmation = palindrome_result(user_input)
    print(confirmation)

if __name__ == '__main__':
    main()
