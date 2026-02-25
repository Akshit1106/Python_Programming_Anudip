# Print tables from 1 to 10
for num in range(1, 11):
    print("Table of", num)
    
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
    
    print()  # Blank line after each table