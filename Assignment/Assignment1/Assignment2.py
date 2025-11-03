print("Enter your account balance:")
balance=float(input())
print("Enter the withdrawal amount:")
withdrawal=float(input())
if withdrawal > balance:
    print("Insufficient Balance")
else:
    print("Transaction Successful")