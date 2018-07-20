
i = [int(input()),int(input()),int(input()),int(input()),int(input())]
a = [0.08,0.139,0.135,1.128,1.483,183,0,0]
b = [0.07,0.130,0.121,1.128,1.483,383,0,0]
c = [0.06,0.108,0.101,1.128,1.483,983,0,0]
m = [a,b,c]
bp = 999999999999
mon = 99999999999

for k in m :
    for n in range(len(i)) :
        k[6] = k[6] + i[n]*k[n]
    if k[6] > k[5]:
        k[7] = k[5] + k[6] - k[5]
    else :
        k[7] = k[5]
    if k[7] < mon :
        bp = k[5]
        mon = k[7]

print(str(bp))
print(int(mon))