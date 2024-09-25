def listMod(lst, p, a):
    lst[p] = e

# ===========================

def add(a, b):
    return a + b

def addTest():
    e=6
    f=4
    res=add(e,f)
    print(e,f,res)

# ===========================

def sumList(ls):
    return ls[0] + ls[1]

def listTest():
    list=[6, 4]
    res=sumList(list)
    print(list[0],list[1],res)

# ===========================

def addFirst(ls, e):
    ls[0:0] = [e]
    # return ls

def addFirstTest():
    list=[7,3,9]
    print(list)
    lstRes=addFirst(list, 5)
    print(list)

# ===========================

def add2(lst, n, v):
    lst[n] = lst[n] + v

def deleteLessThan(lst, v):
    i = 0
    while i < len(lst):
        if lst[i] < v:
            del lst[i]
        else:
            i = i + 1

def testDLT():
    ls = [1,2,3,5,2,3,0]
    print(ls)
    deleteLessThan(ls, 3)
    print(ls)

# ===========================

def deleteLessThan2(lst, v):
    newLst = []
    for e in lst:
        if not (e < v):
            newLst.append(e)
    return newLst

def testDLT2():
    ls = [1,2,3,5,2,3,0]
    print(ls)
    deleteLessThan2(ls, 3)
    print(ls)
    print(newLst)