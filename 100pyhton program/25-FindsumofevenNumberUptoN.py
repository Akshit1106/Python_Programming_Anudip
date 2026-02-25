n = int(input("Enter value of N: "))

i = 1
total = 0

while i <= n:
    if i % 2 == 0:   # Check even
        total += i
    i += 1

print("Sum of even numbers up to", n, "is:", total)