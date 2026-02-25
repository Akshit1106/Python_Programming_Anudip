num = int(input("enter a number: "))
reverse = 0


while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

    print("Reversed number =", reverse)

    #output
    #enter a number = 234
    #reverse number = 432
    