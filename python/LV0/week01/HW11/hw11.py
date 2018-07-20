a1 = float(input())
a2 = float(input())
b1 = float(input())
b2 = float(input())
c1 = float(input())
c2 = float(input())

def sortdata(data1,data2):
    data = [data1,data2]  
    if data[0] > data[1]:
        data = [data2,data1]
    return(data)

a = sortdata(a1,a2)
b = sortdata(b1,b2)
c = sortdata(c1,c2)

if c[0] < b[0]:
    d = b
    b = c
    c = d
if b[0] < a[0]:
    d = a
    a = b
    b = d

left = a[1]
len = a[1] - a[0]

if b[0] >= left:
    len += b[1] - b[0]
    left = b[1]
elif b[0] < left and b[1] > left:
    len += b[1] - left
    left = b[1]

if c[0] >= left:
    len += c[1] - c[0]
    left = c[1]
elif c[0] < left and c[1] > left:
    len += c[1] - left
    left = c[1]

print(int(len))