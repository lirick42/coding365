
def hihi(n, k, ans):
    if n == 1:
        ans.append(k)
        return 0
    elif k < 2**(n-1):
        ans.append(0)
        return hihi(n-1, k, ans)
    elif k >= 2**(n-1):
        ans.append(1)
        return hihi(n-1, 2**n-1-k, ans)

def output(ans):
    for i in ans:
        print(i,end='')
    print()
    return 0

def main():
    ans = []
    str = input()
    str = str.split()
    n = int(str[0])
    k = int(str[1])
    hihi(n, k, ans)
    output(ans)
    while 1 :
        ans = []
        interval = input()
        if interval == '-1':
            break
        else:
            str = input()
            str = str.split()
            n = int(str[0])
            k = int(str[1])
            hihi(n, k, ans)
            output(ans)

main()