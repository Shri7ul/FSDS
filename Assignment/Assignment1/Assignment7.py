color=input("Enter Traffic LIght color: (Red/Yellow/Green) ")
if color.lower()=='red':
    print("Stop")
elif color.lower()=='yellow':
    print("Ready to go")
elif color.lower()=='green':
    print("Go")
else:
    print("Invalid Color")