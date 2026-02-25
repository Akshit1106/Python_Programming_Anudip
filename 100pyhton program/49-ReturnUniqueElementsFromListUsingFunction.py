def unique_elements(lst):
    unique = []
    
    for item in lst:
        if item not in unique:
            unique.append(item)
    
    return unique

# Take list input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Unique elements are:", unique_elements(numbers))