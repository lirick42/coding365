num = input()
num = num.split(' ')
for i in range(len(num)):
    num[i] = int(num[i])

num1 = num[0]
num2 = num[1]
num3 = num[2]

def getTriangel(a,b,c):
    t = [a,b,c]
    d = [0,0,0]
    for i in range(len(d)) : 
        for k in t :    
            if k >= d[i] :
                d[i] = k
        t.remove(d[i])
    
    z = 0  
    for i in d :
        if i <= 0 :
            z = z+1
    if  d[0] >= d[1] + d[2] or  z != 0:
        tri = 'Not Triangle'
    elif d[0]**2 == d[1]**2 + d[2]**2 :
        tri = 'Right Triangle'
    elif d[0]**2 > d[1]**2 + d[2]**2 :
        tri = 'Obtuse Triangle'
    elif d[0]**2 < d[1]**2 + d[2]**2 :
        tri = 'Acute Triangle'
    return(tri)

print(getTriangel(num1,num2,num3))