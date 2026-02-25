numbers = list(map(int, input("Enter numbers: ").split()))

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print("Average is:", average)