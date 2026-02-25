# Take list input from user
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

unique = []  # Empty list to store unique elements

for num in numbers:
    if num not in unique:   # Check if element already exists
        unique.append(num)  # Add only if not present

print("List after removing duplicates:", unique)