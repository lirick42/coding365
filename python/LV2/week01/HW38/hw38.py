class people():
    def __init__(self, name, cata):
        self.name = name
        self.preferList = []
        self.done = 0
        self.cata = cata
        self.partner = None
    def addPrefer(self, str):
        self.preferList.append(str)
    def getname(self):
        return self.name
    def getprefer(self):
        return self.preferList
    def getcata(self):
        return self.cata
    def setPartner(self, partner):
        self.partner = partner
    def getpartner(self):
        return self.partner

def checkPrefer(stuList, num, teaList):
    tempL = [[] for i in range(5)]
    for i in stuList:
        if i.getpartner() == None:
            if i.getprefer()[num] == 'A' and teaList[0].getpartner() == None:
                tempL[0].append(i)
            elif i.getprefer()[num] == 'B' and teaList[1].getpartner() == None:
                tempL[1].append(i)
            elif i.getprefer()[num] == 'C' and teaList[2].getpartner() == None:
                tempL[2].append(i)
            elif i.getprefer()[num] == 'D' and teaList[3].getpartner() == None:
                tempL[3].append(i)
            elif i.getprefer()[num] == 'E' and teaList[4].getpartner() == None:
                tempL[4].append(i)
        else:
            pass
    for index, i in enumerate(tempL):
        if len(i) == 1:
            if index == 0:
                i[0].setPartner(teaList[0].getname())
                teaList[0].setPartner(i[0].getname())
            elif index == 1:
                i[0].setPartner(teaList[1].getname())
                teaList[1].setPartner(i[0].getname())
            elif index == 2:
                i[0].setPartner(teaList[2].getname())
                teaList[2].setPartner(i[0].getname())
            elif index == 3:
                i[0].setPartner(teaList[3].getname())
                teaList[3].setPartner(i[0].getname())
            elif index == 4:
                i[0].setPartner(teaList[-1].getname())
                teaList[-1].setPartner(i[0].getname())
        elif len(i) > 1:
            for target in teaList[index].getprefer():
                end = 0
                for test in i:
                    if target == test.getname():
                        test.setPartner(teaList[index].getname())
                        teaList[index].setPartner(test.getname())
                        end = 1
                        break
                    else:
                        pass
                if end == 1:
                    break
        else:
            pass
def main():
    stuList = []
    teaList = []
    first = input()
    first = first.split(',')
    total = len(first)
    stuList.append(people(chr(90-total+1),'stu'))
    for j in range(total):
        stuList[0].addPrefer(first[j])
    for i in range(1, total):
        temp = input()
        temp = temp.split(',')
        stuList.append(people(chr(90+i-total+1),'stu'))
        for j in range(total):
            stuList[i].addPrefer(temp[j])
    for i in range(total):
        temp = input()
        temp = temp.split(',')
        teaList.append(people(chr(65+i),'tea'))
        for j in range(total):
            teaList[i].addPrefer(temp[j])
    for i in range(total):
        checkPrefer(stuList, i, teaList)
    for i in range(total):
        print("{}->{}".format(stuList[i].getname(),stuList[i].getpartner()))

main()