set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

# Elements present in either set but not both
sym_diff = set1 ^ set2

print("Symmetric difference is:", sym_diff)