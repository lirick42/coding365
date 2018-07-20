tri = int(input())
a = int(input())
out = (a//2)+1

#input 1
def LeftTrianlge(out):
    for i in range(1,out+1):
        for j in range(1,i+1):
            print(j,sep="",end="")
        print()
    for i in range(out,1,-1):
        for j in range(1,i):
            print(j,sep="",end="")
        print()

#input 2
def RightTriangle(out):
    for i in range(1,out+1):
        for k in range(out,i,-1):
            print(".",sep="",end="")
        for j in range(i,0,-1):
            print(j,sep="",end="")
        print()
    for i in range(out-1,0,-1):
        for k in range(out,i,-1):
            print(".",sep="",end="")
        for j in range(i,0,-1):
            print(j,sep="",end="")
        print()

if(tri==1):
    LeftTrianlge(out)
elif(tri==2):
    RightTriangle(out)