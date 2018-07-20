def priority(op):
    if op in ['^']:
        return 3
    if op in ['*', '/']:
        return 2
    if op in ['+', '-']: 
        return 1
    return 0

def main():
    infix = input()
    stack = []
    for ch in infix:
        if ch in ['+', '-', '*', '/', '^']:
            while len(stack) > 0 and priority(ch) <= priority(stack[-1]):
                print(stack.pop(), end='')
            stack.append(ch)
    # 左括弧
        elif ch == '(':
            stack.append(ch)
    # 右括弧
        elif ch == ')':
            while stack[-1] != '(':
                print(stack.pop(), end='')
            stack.pop()
    # 數字
        else:
            print(ch, end='')
    while len(stack) > 0:
        print(stack.pop(), end='')
    print()

if __name__ == '__main__':
    main()