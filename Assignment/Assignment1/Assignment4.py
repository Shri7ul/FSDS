print("Enter your age:")
age=int(input())
if age<5:
    print("Ticket is Free")
elif age>=5 and age<=18:
    print("You have to pay 50% of the ticket price")
elif age>60:
    print("You have to pay 70% of the ticket price")
else:
    print("You have to pay full ticket price")