def b2c(binL):
    count = 0
    dec = 0
    for i in reversed(binL):
        if int(i) == 1:
            dec = dec + 2 ** count
        else:
            pass
        count = count + 1
    return dec

def d2b(num):
    temp = bin(num)
    temp = temp[2:]
    while len(temp) != 4:
        temp = '0'+temp
    return temp

def ddd(data, count = 0):
    if data == 0 or data == 1:
        return count
    elif data % 2 == 0:
        count = count + 1
        data = data / 2
        return ddd(data, count)
    elif data % 2 == 1:
        count = count + 1
        data = (data + 1) / 2
        return ddd(data, count)

def main():
    str = input()
    data = b2c(str)
    ans = ddd(data)
    print(d2b(ans))
    while 1:
        interval = input()
        if interval == '-1':
            break
        else:
            pass
        str = input()
        data = b2c(str)
        ans = ddd(data)
        print(d2b(ans))
main()