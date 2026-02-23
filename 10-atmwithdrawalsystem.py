# ATM Withdrawal System

balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM available cash: "))

if withdraw > 50000:
    print("Withdrawal failed: Daily limit exceeded.")
elif withdraw > balance:
    print("Withdrawal failed: Insufficient account balance.")
elif withdraw > atm_cash:
    print("Withdrawal failed: ATM has insufficient cash.")
else:
    print("Withdrawal successful!")
    print("Remaining balance:", balance - withdraw)