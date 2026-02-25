text = input("Enter a string: ")

upper = 0
lower = 0

# Check each character
for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)