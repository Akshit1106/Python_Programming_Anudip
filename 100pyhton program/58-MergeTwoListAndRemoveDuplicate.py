list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

merged = list1 + list2  # Combine lists
unique = []

for num in merged:
    if num not in unique:
        unique.append(num)

print("Merged list without duplicates:", unique)