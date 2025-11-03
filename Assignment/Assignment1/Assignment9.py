age=int(input("Enter your age: "))
qualification=input("Enter your qualification (highschool/graduate/postgraduate): ")
if age>=18 and qualification.lower()=="graduate":
    print("Eligible for Job")
else:
    print("Not Eligible")
