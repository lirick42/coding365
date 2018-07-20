sBin = int(input())
sNum = int(input())
temp = []

if(2<=sBin<=9 and 0<=sNum<=10000000):
    while(sNum>=sBin):
        temp.append(sNum%sBin)
        sNum = sNum//sBin
    temp.append(sNum)
    for i in range(len(temp),0,-1):
        print(temp[i-1],sep="",end="")
else:
    print(-1)