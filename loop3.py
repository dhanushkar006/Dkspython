print("Prime numbers ")

st=int(input("Enter the start range: "))
end=int(input("Enter the end range: "))

for n in range(st,end+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)
    else:
        print("Invalid")
