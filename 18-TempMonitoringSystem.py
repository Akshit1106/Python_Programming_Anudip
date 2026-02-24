temps = [35, 42, 39, 46, 41, 38]

hottest = max(temps)
coldest = min(temps)

# Replace >45 with Heat Alert
for i in range(len(temps)):
    if temps[i] > 45:
        temps[i] = "Heat Alert"

extreme_days = len([t for t in temps if t != "Heat Alert" and t > 40])

print("Hottest:", hottest)
print("Coldest:", coldest)
print("Updated Temps:", temps)
print("Extreme Days:", extreme_days)

# Output:
# Hottest: 46
# Coldest: 35
# Updated Temps: [35, 42, 39, 'Heat Alert', 41, 38]
# Extreme Days: 2