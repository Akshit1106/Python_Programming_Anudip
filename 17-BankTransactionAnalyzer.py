transactions = [10000, -2000, 15000, -5000, 7000]

balance = sum(transactions)

largest_withdrawal = min(transactions)

deposits_above_10000 = len([t for t in transactions if t > 10000])

print("Balance:", balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits > 10000:", deposits_above_10000)

# Output:
# Balance: 25000
# Largest Withdrawal: -5000
# Deposits > 10000: 1