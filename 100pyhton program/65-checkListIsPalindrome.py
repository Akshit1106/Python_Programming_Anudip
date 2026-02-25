numbers = list(map(int, input("Enter numbers: ").split()))

if numbers == numbers[::-1]:
    print("List is Palindrome.")
else:
    print("List is Not Palindrome.")