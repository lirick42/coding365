from fractions import Fraction
def check0(xFraction):
    for i in range(2):
        if(xFraction[i]==0):
            xFraction[0]=-0.1
xFraction = [int(i) for i in input().split("/")]
yFraction = [int(i) for i in input().split("/")]
check0(xFraction)
check0(yFraction)

if(xFraction[0]==-0.1 or yFraction[0]==-0.1):
    print("ERROR")
    print("ERROR")
else:
    a = Fraction(xFraction[0],xFraction[1])
    b = Fraction(yFraction[0],yFraction[1])
    c = a+b
    cint = int(c)
    d = a*b
    if(cint>0 and c-cint==0):
        print(cint)
    elif(cint<0 and c-cint==0):
        print(cint)
    elif(cint>0 and c-cint!=0):
        print(cint,"(",c-cint,")",sep="")
    elif(cint<0 and c-cint!=0):
        print(cint,"(",abs(c-cint),")",sep="")
    else:
        print(c)
    print(d)