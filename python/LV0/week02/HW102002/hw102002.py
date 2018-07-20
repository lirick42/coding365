aa = []
summ = 0
for i in range(21):
    aa.append(int(input()))
    summ += aa[i]
for i in range(0,18,2):
    if(aa[i]+aa[i+1]==10 and aa[i+1]!=0):
        summ += aa[i+2]
    elif(aa[i]==10 and aa[i+1]==0):
        summ += aa[i+2] + aa[i+3]
print(summ)