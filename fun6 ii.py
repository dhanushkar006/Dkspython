n=int(input("Enter no.of terms: "))
x=int(input("Enter x value: "))

def ser(n,x):
    res=0
    for i in range(1,n+1):
        res=res+(x/(2**i))
    print(res)

ser(n,x)
