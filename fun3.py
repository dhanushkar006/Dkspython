print("1-Sphere \n 2-Cylinder \n 3-Cone \n 4-Rectanguler prism \n 5-triangular prism")
cho=int(input("Enter your choice(1,2,3,4,5): "))

def sphere(pi,r):
    sa=4*pi*r*r
    vol=(4/3)*pi*(r**3)
    print("Surfacearea of the sphere = ",sa)
    print("Volume of the sphere = ",vol)
def cylinder(pi,r,h):
    sa=(2*pi*r*r)+(2*pi*r*h)
    vol=pi*r*r*h
    print("Surfacearea of the cylinder = ",sa)
    print("Volume of the cylinder = ",vol)
def cone(pi,r,s,h):
    sa=(pi*r*s)+(pi*r*r)
    vol=(1/3)*pi*r*r*h
    print("Surfacearea of the cone = ",sa)
    print("Volume of the cone = ",vol)
def recpri(l,h,w):
    sa=2*((l*w)+(l*h)+(w*h))
    vol=l*w*h
    print("Surfacearea of the rectangular prism = ",sa)
    print("Volume of the rectanguler prism = ",vol)
def tripri(b,h,s,l):
    sa=((b*h)+2*(l*s)+(l*b))
    vol=(1/2)*(b*l)*h
    print("Surfacearea of the triangular prism = ",sa)
    print("Volume of the triangular prism = ",vol)

if cho==1:
    r=int(input("Enter radius: "))
    sphere(3.14,r)
elif cho==2:
    r=int(input("Enter radius: "))
    h=int(input("Enter height: "))
    cylinder(3.14,r,h)
elif cho==3:
    r=int(input("Enter radius: "))
    h=int(input("Enter height: "))
    s=int(input("Enter slantheight: "))
    cone(3.14,r,s,h)
elif cho==4:
    l=int(input("Enter length: "))
    w=int(input("Enter width: "))
    h=int(input("Enter height: "))
    recpri(l,h,w)
elif cho==5:
    b=int(input("Enter breadth: "))
    h=int(input("Enter height: "))
    l=int(input("Enter length: "))
    s=int(input("Enter slantheight: "))
    tripri(b,h,s,l)
else:
    print("Invalid entry")
