# Hospital Emergency Triage

heart_rate = int(input("Enter heart rate: "))
severe_injury = input("Severe injury? (yes/no): ")
age = int(input("Enter age: "))

if heart_rate < 60 or heart_rate > 100 or severe_injury.lower() == "yes":
    category = "Critical"
elif age > 65:
    category = "Moderate (Upgraded Priority)"
else:
    category = "Normal"

print("Patient Category:", category)