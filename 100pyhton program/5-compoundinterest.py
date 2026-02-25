p = float(input("enter Principal: "))
r = float(input("enter rate: "))
t = float(input("enter time: "))

amount = p * (1 + r/100)** t 
ci = amount - p

print("Compound interest =", ci)


#output
#ci will be calculated