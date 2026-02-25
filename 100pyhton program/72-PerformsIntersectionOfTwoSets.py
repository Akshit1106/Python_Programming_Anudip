set1 = set(map(int, input("Enter first set elements: ").split()))
set2 = set(map(int, input("Enter second set elements: ").split()))

intersection_set = set1 & set2  # Intersection operation

print("Intersection of sets is:", intersection_set)