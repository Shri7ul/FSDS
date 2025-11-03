amount=int(input("Enter the amount: "))
if amount>=1000:
    discount=amount*0.1
    final_amount=amount-discount
    print("Final bill amount.:",final_amount)
else:
    print("No discount")