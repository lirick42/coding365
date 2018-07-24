def foot(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    elif n == 2:
        return 2
    else:
        return foot(n-1) + foot(n-2) + foot(n-3)
def main():
    num = int(input())
    print(foot(num))

main()