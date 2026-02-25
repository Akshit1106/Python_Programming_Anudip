def maximum(a, b, c):
    max_num = a
    
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    
    return max_num

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Maximum number is:", maximum(a, b, c))