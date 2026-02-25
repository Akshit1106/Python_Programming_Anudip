set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

union_set = set1 | set2  # Union operation

print("Union of sets is:", union_set)