numbers = list(map(int, input("Enter numbers: ").split()))

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0  # Replace negative with zero

print("Updated list:", numbers)