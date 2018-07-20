import math

a = float(input())
b = float(input())
c = float(input())

if b**2-4*a*c >= 0:
	
    t = math.sqrt(b**2-4*a*c)
    x1 = int((-b+t)/(2*a)*10)
    x2 = int((-b-t)/(2*a)*10)
    print("%.1f" % (x1/10))
    print("%.1f" % (x2/10))

else:

    t = math.sqrt(abs(b**2-4*a*c))
    x11 = int(-b/(2*a)*10)
    x11 = str("%.1f"% (x11/10))
    x22 = int(t/(2*a)*10)

    if x22 > 0:

        x22 = str("%.1f"% (x22/10))
        print(x11 + "+" + x22 + 'i')
        print(x11 + "-" + x22 + 'i')

    elif x22 < 0 :

        x22 = str("%.1f"% (-x22/10))
        print(x11 + "-" + x22 + 'i')
        print(x11 + "+" + x22 + 'i')