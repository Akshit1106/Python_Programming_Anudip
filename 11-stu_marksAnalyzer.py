# Student Marks Analyzer

marks = [95, 102, 67, -5, 88, 76, 54, 120, 89]

# Remove invalid marks
valid_marks = [m for m in marks if 0 <= m <= 100]

# Calculate average
average = sum(valid_marks) / len(valid_marks)

# Find topper
topper = max(valid_marks)

# Display grades
grades = []
for m in valid_marks:
    if m >= 90:
        grades.append("A")
    elif m >= 75:
        grades.append("B")
    elif m >= 50:
        grades.append("C")
    else:
        grades.append("Fail")

print("Valid Marks:", valid_marks)
print("Average:", average)
print("Topper:", topper)
print("Grades:", grades)

# Output:
# Valid Marks: [95, 67, 88, 76, 54, 89]
# Average: 78.16666666666667
# Topper: 95
# Grades: ['A', 'C', 'B', 'B', 'C', 'B']