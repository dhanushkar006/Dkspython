n=int(input("Enter no.of terms: "))
def ser(n):
    res=0
    r=15
    su=0
    for i in range(1,n+1):
        res=res+r
        su=su+res
    print(su)
ser(n)
    
