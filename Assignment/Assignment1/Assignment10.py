unit=float(input("Enter the unit consumed: "))
if unit<=100:
    bill=unit*5
elif unit>100 and unit<=200:
    bill=100*5+(unit-100)*7
else:
    bill=100*5+100*7+(unit-200)*10
    
print("total payable amount.:",bill)