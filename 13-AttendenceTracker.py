# Attendance Tracker

# 1 = Present, 0 = Absent
attendance = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0]

# Step 1: Calculate attendance percentage
total_days = len(attendance)
present_days = attendance.count(1)

percentage = (present_days / total_days) * 100

print("Attendance Percentage:", percentage)


# Step 2: Check if attendance is below 75%
if percentage < 75:
    print("Warning: Attendance below 75%")
else:
    print("Good Attendance")


# Step 3: Replace consecutive absences with 'Warning'
for i in range(len(attendance) - 1):
    if attendance[i] == 0 and attendance[i + 1] == 0:
        attendance[i] = "Warning"
        attendance[i + 1] = "Warning"

print("Updated Attendance List:", attendance)


# Output:
# Attendance Percentage: 50.0
# Warning: Attendance below 75%
# Updated Attendance List: [1, 1, 'Warning', 'Warning', 1, 0, 1, 1, 'Warning', 'Warning']