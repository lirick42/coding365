import math
#Please enter the number a 
a = input()
#Please enter the number b
b = input()
#Please enter the number c
c = input()
#set a,b,c to int type
a = int(a)
b = int(b)
c = int(c)
#x1,x2 calc
x1 = ((-b)+ math.sqrt(b*b-4*a*c))/(2*a)
x2 = ((-b)- math.sqrt(b*b-4*a*c))/(2*a)
x1 = int(x1*10)
x2 = int(x2*10)
#print the asn
print("%.1f" % (x1/10))
print("%.1f" % (x2/10))