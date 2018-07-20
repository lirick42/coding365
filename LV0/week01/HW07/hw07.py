
a = int(input())
b = int(input())
c = int(input())

mon = 0

if a >= 1 and a <=10:
    mon += a*380
elif a > 10 and a <=20:
    mon += a*380*0.9
elif a > 20 and a <= 30:
    mon += a*380*0.85
elif a > 30:
    mon += a*380*0.8

if b >= 1 and b <=10:
    mon += b*1200
elif b > 10 and b <=20:
    mon += b*1200*0.95
elif b > 20 and b <= 30:
    mon += b*1200*0.85
elif b > 30:
    mon += b*1200*0.8

if c >= 1 and c <=10:
    mon += c*180
elif c > 10 and c <=20:
    mon += c*180*0.85
elif c > 20 and c <= 30:
    mon += c*180*0.8
elif c > 30:
    mon += c*180*0.7

print(int(mon))