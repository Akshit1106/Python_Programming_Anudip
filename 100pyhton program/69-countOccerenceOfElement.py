numbers = tuple(map(int, input("Enter tuple elements: ").split()))
element = int(input("Enter element to count: "))

count = 0

for num in numbers:
    if num == element:
        count += 1

print("Occurrence of element is:", count)