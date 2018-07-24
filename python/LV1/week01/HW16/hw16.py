#將字串(str) 反轉後放入到 List(int)
def cS2L(List):
    temp = []
    for i in range(len(List)):
        temp.append(List[i])
    temp.reverse()
    temp = list(map(int, temp))
    return temp

#將輸入之兩數字補 0 至相同長度
def pZero(numA, numB):
    for i in range((abs(len(numA) - len(numB)))):
        if (len(numA) < len(numB)):
            numA.append(0)
        else:
            numB.append(0)
    return numA, numB

#加法
def add(add, added):
    carry = 0
    ans = []
    for i in range(len(add)):
        digit = add[i] + added[i] + carry
        if digit >= 10:
            digit = digit - 10
            carry = 1
        else:
            carry = 0
        ans.append(digit)

    if (carry == 1):
        ans.append(1)
    ans.reverse()
    return ans

#減法
def sub(sub, subed):
    borrow = 0
    ans = []
    for i in range(len(sub)):
        digit = sub[i] - subed[i] + borrow
        if digit < 0:
            digit = digit + 10
            borrow = -1
        else:
            borrow = 0
        ans.append(digit)
    ans = delZero(ans)
    return ans


#將多餘的 0 刪除
def delZero(list):
    list.reverse()
    for i in range(len(list)):
        if list[0] == 0 and len(list) != 1:
            del (list[0])
        else:
            break
    return list


#印出答案
def printans(list):
    for i in list:
        print(i, end='')
    print("")


#例外處理：超過 10 位元
def overC(calculation):
    for i in range(len(calculation)):
        if (calculation[i] >= 10):
            calculation[i + 1] = calculation[i + 1] + calculation[i] // 10
            calculation[i] = calculation[i] % 10
    return calculation


#乘法
def adjAns(calculation):
    calculation = overC(calculation)
    calculation = delZero(calculation)
    return calculation

def multiply(multiplier, multiplicand):
    calculation = []
    for i in range(120):
        calculation.append(0)
    for i in range(len(multiplier)):
        for j in range(len(multiplicand)):
            num1 = multiplicand[i] * multiplier[j]
            if (calculation[i + j] == 0):
                calculation[i + j] = num1
            else:
                calculation[i + j] = calculation[i + j] + num1
    calculation = adjAns(calculation)
    return calculation


# 若輸入超過 60 位數，則回傳 ERROR
def isCorrectInputNumber(num1, num2):
    if len(num1) > 60 or len(num2) > 60:
        print("input Error")
        return False
    else:
        return True


num1 = ""
num2 = ""

while True:
    num1 = input()
    num2 = input()
    if (isCorrectInputNumber(num1, num2)):
        break

num1 = cS2L(num1)
num2 = cS2L(num2)
num1, num2 = pZero(num1, num2)
printans(add(num1, num2))
printans(sub(num1, num2))
printans(multiply(num1, num2))
