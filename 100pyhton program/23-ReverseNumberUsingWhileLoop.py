num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10          # Get last digit
    reverse = reverse * 10 + digit
    num //= 10                # Remove last digit

print("Reversed number is:", reverse)