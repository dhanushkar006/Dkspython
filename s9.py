print("....Restaurant Tip Calculator....")
print("1-Bad \n 2-Not bad \n 3-Average \n 4-Good \n 5-Excellent")
food=int(input("Enter food rating(1-5): "))
ser=int(input("Enter service rating(1-5): "))
am=int(input("Enter ambience rating(1-5): "))
bill=int(input("Enter your bill amount: "))

if food==4 or food==5:
    if ser==4 or am==4 or ser==5 or am==5:
        tip=bill*(10/100)
        print("Tips = ",tip)
    else:
        tip=bill*(5/100)
        print("Tips = ",tip)

if food==1 or food==2 or food==3:
    if ser==4 or am==4 or ser==5 or am==5:
        tip=bill*(5/100)
        print("Tips = ",tip)
    else:
        tip=bill*(1/100)
        print("Tips = ",tip)
