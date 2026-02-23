# E-commerce Discount Engine

cart_value = float(input("Enter cart value: "))
membership = input("Enter membership (Silver/Gold/Platinum): ")
festival = input("Is it festival season? (yes/no): ")

discount = 0

# Cart based discount
if cart_value > 10000:
    discount = 10
elif cart_value > 5000:
    discount = 5

# Membership discount
if membership.lower() == "silver":
    discount = max(discount, 5)
elif membership.lower() == "gold":
    discount = max(discount, 10)
elif membership.lower() == "platinum":
    discount = max(discount, 15)

# Festival discount
if festival.lower() == "yes":
    discount = max(discount, 20)

final_amount = cart_value - (cart_value * discount / 100)

print("Highest Discount Applied:", discount, "%")
print("Final Payable Amount:", final_amount)