# Function to check palindrome
def is_palindrome(text):
    if text == text[::-1]:   # Reverse string check
        return True
    return False

text = input("Enter a string: ")

if is_palindrome(text):
    print("It is a Palindrome.")
else:
    print("It is not a Palindrome.")