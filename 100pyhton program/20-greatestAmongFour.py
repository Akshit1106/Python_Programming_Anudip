# Take four numbers from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

# Assume first number is greatest
greatest = a

# Compare with other numbers
if b > greatest:
    greatest = b
if c > greatest:
    greatest = c
if d > greatest:
    greatest = d

# Print result
print("The greatest number is:", greatest)