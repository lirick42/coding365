data = input()
data = data.split(' ')

for i in range(len(data)):
    data[i] = int(data[i])

#計算平均值
datasum = sum(data)/5*100   
datasum = int(datasum)/100
print("%.2f" % datasum)

var = 0
for k in data:
    var = var + (k-datasum)**2   

#計算變異數
var = var/5
dev = var**0.5 
var = var*100
var = int(var)/100
print("%.2f" % var)

#計算標準差
dev = dev*100  
dev = int(dev)/100
print("%.2f" % dev)
