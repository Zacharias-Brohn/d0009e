import string

class LoadError(Exception):
    def __init__(self):
        pass
    return

def save(filename, memory):
    f = open(filename,'w')
    f.write("Savefile for calc example in D0009E\n")
    for var in memory:
        f.write(var+"="+str(memory[var])+"\n")
    f.close()

def load(filename):
    memory = {}
    f = open(filename,'r')
    f.readline()
    while True:
        line = f.readline()
        if line == '':
            break
        [var, value] = line.split('=')
        memory[var] = int(value)
    f.close()
    return memory

def calc():
    print('Summera')
    sum = 0
    memory = load('calc.ini')
    while True:
        s = input()
        if s == '':
            printSum(sum)
            sum = 0
        elif s[0] == 'E':
            save('calc.ini',memory)
            break
        elif s[0] == '=':
            storeAndPrint(s[1], sum, memory)
            sum = 0
        elif 'a' <= s[0] <= 'z':
            sum += memory[s[0]]
        else:
            sum += int(s)

def calc2():
    try:
        memory = load('calc.ini')
    except LoadError:
        memory = {}
    while True:
        s=input()
        if s == '':
            printSum(sum)
            sum = 0
        elif s[0] == 'E':
            save('calc.ini',memory)
            break
        elif s[0] == '=':
            try:
                storeAndPrint()

def storeAndPrint(var,sum,memory):
    if 'a' <= var <= 'z':
        print(sum,'(stored as',var,')')
        print('-'*10)
        memory[var] = sum

def printSum(sum):
    print(sum)
    print('-'*10)

calc()