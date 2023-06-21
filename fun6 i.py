n=int(input("Enter no.on terms: "))

def fac(n):
    res=0
    fact=1
    for i in range(1,n+1):
        fact*=i
        res=res+(i/fact)
    print(res)
fac(n)
