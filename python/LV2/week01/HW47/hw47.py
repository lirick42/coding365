from fractions import Fraction
n = int(input())
numA = []
numB = []
for row in range(n):
    n = list(map(int, input().split()))
    numA.append(n)
    numB.append(n)
for row in range(0, len(numA)):
    for k in range(1, len(numA)):
        a = -1 * (Fraction(numA[(row+k) % len(numA)][row])/Fraction(numA[row][row]))
        for j in range(len(numA[0])):
            numB[(row+k) % len(numA)][j] = numA[row][j] * a + numA[(row+k) % len(numA)][j]
    numA = numB.copy()
for row in range(len(numA)):
    print('X[{}]='.format(row+1) + str(numA[row][-1] / numA[row][row]))