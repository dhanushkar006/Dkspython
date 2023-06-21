name=input("Enter name: ")
gen=input("Enter gender(M/F): ")
age=int(input("Enter age: "))
da=int(input("Enter your total no.of working days: "))

if age>=18 and age<30 and gen=='M':
    print("Wage = ",da*700)
elif age>=18 and age<30 and gen=='F':
     print("Wage = ",da*750)
elif age>=30 and age<=40 and gen=='M':
     print("Wage = ",da*800)
elif age>=30 and age<=40 and gen=='F':
     print("Wage = ",da*850)
else:
    print("Invalid")
