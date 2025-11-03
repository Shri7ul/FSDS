temperature=float(input("Enter temperature in Celsius: "))
if temperature<10:
    print("It's too Cold")
elif temperature>=10 and temperature<=25:
    print("It's cool outside")
else:
    print("It's Hot outside")