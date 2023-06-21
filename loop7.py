print("Armstrong number")

st=int(input("Enter the start num: "))
en=int(input("Enter the end num: "))
for i in range(st,en+1):
    sum=0
    temp=i
    while i!=0:
        n=i%10
        sum+=n**3
        i=i//10
    if temp==sum:
        print(sum)
