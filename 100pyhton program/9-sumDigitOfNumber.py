num = int(input("enter a number: "))
sum_digit = 0

while num > 0:
    digit = num % 10
    sum_digit += digit
    num //= 10

print ("sum of digit =", sum_digit)

#output
#enter a number= 37
# 3 + 7 = 10
