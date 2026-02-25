students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Find topper
topper = max(students, key=students.get)

print("Topper is:", topper)
print("Marks:", students[topper])