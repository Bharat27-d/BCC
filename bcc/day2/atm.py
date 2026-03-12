balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))
if withdraw <= balance:
        balance -= withdraw
        print("Transaction done")
        print(f"Remaining balance: {balance}")
else:
        print("Insufficient balance")