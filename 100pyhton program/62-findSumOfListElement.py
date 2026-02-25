numbers = list(map(int, input("Enter numbers: ").split()))

total = 0

for num in numbers:
    total += num

print("Sum of list elements is:", total)