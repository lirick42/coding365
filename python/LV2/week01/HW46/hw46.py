n = int(input())
k = []
dire = [(1,0),(-1,0),(0,-1),(0,1)]
for i in range(n):
    j = input().split()
    k.append(j)

def boo(now, used):
    if now == (n-2,n-2):
        used.append((n-2,n-2))
        return used
    for i in dire:
        boo1 = k[ now[0] + i[0]][ now[1] + i[1]]
        if boo1 != '1' :
            if (now[0] + i[0], now[1] + i[1]) in used:
                pass
            else:
                used.append(now)
                used1 = used.copy()
                ans = boo((now[0]+i[0],now[1]+i[1]),used1)
                if ans != False:
                    return ans
    return False 
     
point = boo((1,1),[])

for i in point:
    k[i[0]][i[1]] = '#'
for i in k:
    print(*i)