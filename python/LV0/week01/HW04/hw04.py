num = input()
num = num.split(' ')
for i in range(len(num)):
    num[i] = int(num[i])


num1 = num[0]
num2 = num[1]
num3 = num[2]

def getTriangel(data1,data2,data3): 
    row_data = [data1,data2,data3]  
    sort_data = [0,0,0] 

    for i in range(len(sort_data)) : 
        for k in row_data :    
            if k >= sort_data[i] :
                sort_data[i] = k 
        row_data.remove(sort_data[i])

    z = 0  

    for i in sort_data :
        if i <= 0 :
            z = z+1  
    if  sort_data[0] >= sort_data[1] + sort_data[2] or  z != 0:
        tri = 1
    elif sort_data[0] == sort_data[1] and sort_data[1] == sort_data[2]:
        tri = 2
    elif (sort_data[0] == sort_data[1] and sort_data[1] != sort_data[2] and sort_data[0]**2 + sort_data[1]**2 > sort_data[2]**2) or (sort_data[1] == sort_data[2] and sort_data[1] != sort_data[2] and sort_data[1]**2 + sort_data[2]**2 > sort_data[0]**2):
        tri = 3
    else:
        tri = 4

    return(tri)

print(getTriangel(num1,num2,num3))