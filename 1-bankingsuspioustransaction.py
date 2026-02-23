# Banking – Suspicious Transaction Detection

amount = float(input("Enter transaction amount: "))
account_age = int(input("Enter account age in months: "))
international = input("Is the transaction international? (yes/no): ")

if amount > 200000 and account_age < 6 and international.lower() == "yes":
    print("Transaction flagged for manual verification.")
else:
    print("Transaction is normal.")