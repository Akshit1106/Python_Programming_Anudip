def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

print("Result is:", power(base, exp))