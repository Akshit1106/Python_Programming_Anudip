# Take two sets as input
set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

# Difference means elements in set1 but not in set2
difference = set1 - set2

print("Difference of sets is:", difference)