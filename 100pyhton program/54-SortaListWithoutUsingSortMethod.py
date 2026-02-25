numbers = list(map(int, input("Enter numbers: ").split()))

# Bubble sort logic
for i in range(len(numbers)):
    for j in range(0, len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            # Swap elements
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Sorted list is:", numbers)