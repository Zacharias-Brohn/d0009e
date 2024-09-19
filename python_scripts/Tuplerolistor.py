'''
for x in list:
    ...

(k,v) = tupel
    if k == 'SMD':
        return

Dictionary/Database
Kataloger kan ha index med valfri icke muterbar typ.
Index: string, float, int, pair of integers, pair of strings and integers, booleans, etc.
'''

eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
print(eng2sp)
print(list(eng2sp.values()))
print(list(eng2sp.keys()))
print(list(eng2sp.items()))

inventory = {'apples':430,'bananas':312,'oranges':525,'pears':217}
print(inventory)
inventory['pears'] = 0 #Om päron slutsäljs
print(inventory)
inventory['pears'] = 217
del inventory['pears'] #Om päron försvinner helt från sortimentet
print(inventory)
# Will error: print(inventory['pears'])
inventory['oranges'] + 17 #Funkar bara om oranges redan finns
inventory['pineapples'] = 50
print(inventory)

print('bananas' in inventory)
print('pears' in inventory)

def sumFromTo(start,stop):
    if start==stop:
        return start
    return start + sumFromTo(start+1,stop)

def sumFromTo2(start,stop):
    if start==stop:
        return start
    return stop + sumFromTo(start,stop-1)

def sum(lst):
    if len(lst)==0:
        return 0
    else:
        return lst[0]+sum(lst[1:])

lst=[1,1,2]
print(sum(lst))

def countLarger(lst,e):
    if len(lst)==0:
        return 0
    else:
        if lst[0]>e:
            return 1+countLarger(lst[1:],e)
        else:
            return countLarger(lst[1:],e)

def sumIterative(lst):
    v = 0
    for e in lst:
        v += e
    return v

#List mutation
a=[1,3,5,7]
b=a           # Mirrors list/Alias
print(b)
a[1]=2
print(b)
b[2]=3
print(a)
c=a[:]        # Copies list
a[3]=4
print(c)
print(a)
a=[1,3,5,7,8] # Changes reference, not the list
print(a)
print(b)

def deleteHead(list):
    list[0:1] = []  # Does not return anything

numberlist = [1,8,4,2]
print(f"\n{numberlist}")
deleteHead(numberlist)
print(numberlist)   # But because of aliasing, it still removes a list item