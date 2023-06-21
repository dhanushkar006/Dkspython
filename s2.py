a,b,c=map(int,input("Enter the sides with space").split())
if (a+b)>=c and (a+c)>=b and (b+c)>=a:
    print("triangle possible")
else:
    print("not possible")
