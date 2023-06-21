name=input("Enter your name: ")
sa=int(input("Enter your salary: "))
yr=int(input("Enter your years of service: "))
if yr>=10:
    bonus=sa*(10/100)
    t=sa+bonus
    print("Your bonus is: ",t)
elif yr>=6 or yr<=9:
    bonus=sa*(8/100)
    t=sa+bonus
    print("Your bonus is: ",t)
elif yr<=5:
    bonus=sa*(5/100)
    t=sa+bonus
    print("Your bonus is: ",t)

else :
    print("Sorry you don't have enough years of experience")
