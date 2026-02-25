weight = float(input("enter weight in kg: "))
height = float(input("Enter a height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("Normal Weight")
elif bmi < 30:
    print("overweight")
else:
    print("odese")



