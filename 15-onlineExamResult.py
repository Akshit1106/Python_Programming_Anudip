scores = [25, 32, 45, 30, 38, 50, 29]

# Remove lowest 2 scores
scores.sort()
scores = scores[2:]

# Add grace marks
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

# Count pass (>=40)
passed = len([s for s in scores if s >= 40])

print("Updated Scores:", scores)
print("Students Passed:", passed)

# Output:
# Updated Scores: [35, 38, 45, 50]
# Students Passed: 