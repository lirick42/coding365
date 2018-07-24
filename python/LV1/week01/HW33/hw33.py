line = int(input())

data = line.split(' ')
N, M, K = map(int, data)

people = [i for i in range(1, N+1)]

#爆炸者的位置
index = 0
for i in range(K):
    #從現在向後數M個人，找到爆炸者，將它移除
    #每一次爆炸串列會少一個人，所以減1
    index = (index + M - 1) % len(people)
    del people[index]
    #若刪除恰好最末元素，刪除完畢後，此時索引值移到最前頭(0)
    if index == len(people):
        index = 0
print(people[index])