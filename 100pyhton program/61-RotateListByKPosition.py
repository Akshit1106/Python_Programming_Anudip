numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter number of positions to rotate: "))

k = k % len(numbers)  # Handle large K

rotated = numbers[-k:] + numbers[:-k]

print("Rotated list is:", rotated)