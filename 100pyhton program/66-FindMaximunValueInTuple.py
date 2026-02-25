numbers = tuple(map(int, input("Enter tuple elements: ").split()))

max_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num

print("Maximum value is:", max_value)