height = int(input())
n = height//2+1

for i in range(n):
    for k in range(i+1,n):
        print(".",sep="",end="")
    for j in range(2*i+1):
        print("*",sep="",end="")
    for k in range(i,n-1):
        print(".",sep="",end="")
    print()

for i in range(n-1,0,-1):
    for k in range(n,i,-1):
        print(".",sep="",end="")
    for j in range(1,2*i):
        print("*",sep="",end="")
    for k in range(n,i,-1):
        print(".",sep="",end="")    
    print()