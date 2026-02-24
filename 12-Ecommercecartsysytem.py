prices = [2000, 1500, 2000, 1000, 500]

# Remove duplicates
prices = list(set(prices))

total = sum(prices)

# Apply 10% discount if total > 5000
if total > 5000:
    total *= 0.9

# Add 18% GST
total *= 1.18

print("Final Amount:", total)

# Output:
# Final Amount: 5310.0