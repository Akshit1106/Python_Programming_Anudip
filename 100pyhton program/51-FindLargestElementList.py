numbers = list(map(int, input("Enter numbers: ").split()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element is:", largest)