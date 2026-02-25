numbers = tuple(map(int, input("Enter tuple elements: ").split()))

min_value = numbers[0]

for num in numbers:
    if num < min_value:
        min_value = num

print("Minimum value is:", min_value)