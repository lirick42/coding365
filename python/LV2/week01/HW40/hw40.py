class node:
    def __init__(self, num):
        self.num = num
        self.father = None
        self.left = None
        self.right = None
    def setRg(self, right):
        self.right = right
    def setLf(self, left):
        self.left = left
    def setFa(self, father):
        self.father = father
    def getRg(self):
        return self.right
    def getLf(self):
        return self.left
    def getFa(self):
        return self.father
    def getNumber(self):
        return self.num
    def isroot(self):
        if self.father == None:
            return True
        else:
            return False

def insNode(nodeL):
    num = int(input())
    if len(nodeL) == 0:
        rootNode = node(num)
        nodeL.append(rootNode)
    else:
        rootNode = nodeL[0]
        temp = rootNode
        target = node(num)
        while 1:
            if num > temp.getNumber():
                if temp.getRg() == None:
                    temp.setRg(target)
                    target.setFa(temp)
                    break
                else:
                    temp = temp.getRg()
            elif num <= temp.getNumber():
                if temp.getLf() == None:
                    temp.setLf(target)
                    target.setFa(temp)
                    break
                else:
                    temp = temp.getLf()

def inorderPrint(rootNode):
    if(rootNode == None):
        return 0
    inorderPrint(rootNode.getLf())
    print(rootNode.getNumber(),end=' ')
    inorderPrint(rootNode.getRg())

def main():
    nodeL = []
    while 1:
        str = input()
        if str == 'e':
            break
        elif str == 'p':
            try:
                inorderPrint(nodeL[0])
                print()
            except IndexError:
                print('null')
        elif str == 'i':
            insNode(nodeL)

main()