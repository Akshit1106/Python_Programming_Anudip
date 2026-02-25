numbers = tuple(map(int, input("Enter tuple elements: ").split()))

if len(numbers) == len(set(numbers)):
    print("All elements are unique.")
else:
    print("Elements are not unique.")