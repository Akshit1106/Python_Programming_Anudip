set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

# Check if set1 is subset of set2
if set1.issubset(set2):
    print("First set is a subset of second set.")
else:
    print("First set is NOT a subset of second set.")