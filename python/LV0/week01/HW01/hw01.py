#輸入姓名
name = input('')
#輸入學號
ids = input('')
#輸入國文成績
chinese = input('')
#輸入計算機概論成績
cs = input('')
#輸入計算機程式成績
codev = input('')
#加總
sum = int(chinese) + int(cs) + int(codev)
#計算平均
avg = sum / 3
#印出資料
print ("Name:"+name)
print ("Id:"+ids)
print ("Total:%d"%(sum))
print ("Average:%d"%(avg))