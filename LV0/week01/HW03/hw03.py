import math
#輸入數值 1
num1 = input() 
#輸入數值 2
num2 = input() 
#轉為 float
num1 = float(num1) 
num2 = float(num2)
#加
sum_num12 = int((num1+num2)*100) 
print('Sum:%.2f' % (sum_num12/100)) 
#減
dif = int(abs(num1-num2)*100)
print('Difference:%.2f' % (dif/100))
#乘
pro = int(num1*num2*100)
print('Product:%.2f' % (pro/100))
#除
quo = int(num1/num2*100)
print('Quotient:%.2f' % (quo/100))