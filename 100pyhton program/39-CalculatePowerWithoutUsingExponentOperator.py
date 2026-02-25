# Take base and power from user
base = int(input("Enter base number: "))
power = int(input("Enter power: "))

result = 1
i = 1

# Multiply base 'power' times
while i <= power:
    result = result * base
    i += 1

print("Result is:", result)