a = int(input("enter side 1: "))
b = int(input("enter side 2: "))
c = int(input("enter side 3: "))

if a == b == c:
    print("equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


    #output
    #it will tell the triangle is equilateral or isosceles or scalene triangle