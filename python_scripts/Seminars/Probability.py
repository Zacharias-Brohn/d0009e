import random

def printLuckor(luckList):
    for i in rand(1,len(luckList)+1):
        printStr=str(i)
        if len(printStr)<2:
            printStr = ' '+printStr
        print(printStr, end=' ')
    print()
    for lucka in luckList:
        if isOpen(lucka):
            if isWin(lucka):
                print(' X', end=' ')
            else:
                print(' -', end=' ')
        else:
            print(" ?", end=' ')
    print()

def printChoice(n):
    s = ' '*3*(n-1)+" |"
    print(s)

def isOpen(lucka):
    return lucka[0]

def isWin(lucka):
    return lucka[1]

def setOpen(lucka, state):
    lucka[0] = state

def openAllNotWinNotChoice(luckList, choice):
    for lucka in luckList:
        if not isOpen(lucka) and not isWin(lucka):
            setOpen(lucka, True)
    setOpen(luckList[choice], False)

    if luckList[choice][1]:
        closeAlso = choice
        while closeAlso == choice:
            closeAlso = int(random.random()*len(luckList))
        setOpen(luckList[closeAlso], False)

def openAll(luckList):
    for lucka in luckList:
        lucka[0] = True

def findUnopened(luckList, choice):
    n = 0
    while n < len(luckList):
        if not isOpen(luckList[n]) and not n == choice:
            return n 
        n = n+1

def uIchooseLucka(luckList):
    printLuckor(luckList)
    n = int(input("Lucka: "))
    printLuckor(luckList)
    printChoice(n)
    return n

def uIopenAllNotWin(luckList, n):
    input("Öppna lucka: ")
    openAllNotWinNotChoice(luckList, n-1)
    printLuckor(luckList)
    printChoice(n)

def uIchangeLucka(luckList, n):
    ans = input("Vill du byta lucka? (ja/nej): ")
    if ans == "ja":
        

def uIshowResult():


def runGame():
    nLuck = int(input("Antal luckor: "))
    luckList = [[]]*nLuck
    for i in range(nLuck):
        luckList[i] = [False, False]
    luckList[int(random.random()*nLuck)][1] = True
    n = uIchooseLucka(luckList)
    uIopenAllNotWin(luckList,n)
    n = uIchangeLucka(luckList,n)
    uIshowResult(luckList,n)

def main():
    while True:
        runGame()
        if input("Spela igen? (ja/nej) ") != "ja":
            break