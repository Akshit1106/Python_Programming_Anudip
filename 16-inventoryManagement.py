stock = [0, 5, 20, 8, 15]

# Remove 0 stock
stock = [s for s in stock if s != 0]

# Add restock 50 to items below 10
for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

total_inventory = sum(stock)

print("Updated Stock:", stock)
print("Total Inventory:", total_inventory)

# Output:
# Updated Stock: [55, 20, 58, 15]
# Total Inventory: 148