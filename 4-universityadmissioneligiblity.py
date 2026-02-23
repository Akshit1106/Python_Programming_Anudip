# University Admission Eligibility

percentage = float(input("Enter 12th percentage: "))
maths = input("Did you study Mathematics? (yes/no): ")
entrance_score = float(input("Enter entrance exam score: "))

if percentage < 75:
    print("Not eligible: Minimum 75% required.")
elif maths.lower() != "yes":
    print("Not eligible: Mathematics is required.")
elif entrance_score < 80:
    print("Not eligible: Entrance score must be at least 80.")
else:
    print("Congratulations! You are eligible for admission.")