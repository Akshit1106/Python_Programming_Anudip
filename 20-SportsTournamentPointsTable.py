points = [10, -5, 25, 15, -2]

# Replace negative with 0
points = [p if p >= 0 else 0 for p in points]

points.sort(reverse=True)

winner = points[0]
runner_up = points[1]

print("Leaderboard:", points)
print("Winner Points:", winner)
print("Runner-up Points:", runner_up)

# Output:
# Leaderboard: [25, 15, 10, 0, 0]
# Winner Points: 25
# Runner-up Points: 15