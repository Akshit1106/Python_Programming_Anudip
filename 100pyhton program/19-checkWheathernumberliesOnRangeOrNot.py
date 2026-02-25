# Take the number from the user
number = int(input("Enter the number to check: "))

# Take the lower limit of the range
lower = int(input("Enter the lower limit of the range: "))

# Take the upper limit of the range
upper = int(input("Enter the upper limit of the range: "))

# Check whether the number lies between lower and upper (inclusive)
if lower <= number <= upper:
    print("Yes, the number lies within the range.")
else:
    print("No, the number does not lie within the range.")