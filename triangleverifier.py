angle1 = float(input("enter angle 1:"))
angle2 = float(input("enter angle 2:"))
angle3 = float(input("enter angle 3:"))
# check condition

if angle1 > 0 and angle2 > 0 and angle3 > 0 and ( angle1 + angle2 + angle3 == 180):
    print("The angles form a triangle.")
else:
    print("The angle form a triangle.")