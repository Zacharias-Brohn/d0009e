def sumFromToIterative(start, stop):
    sum = 0
    for i in range(start, stop+1):
        sum = sum + i
    return sum

iterativeResult = sumFromToIterative(4, 8)
print(iterativeResult)

def sumFromToRecursive(start, stop):
    if start > stop:
        return 0
    else:
        return start + sumFromToRecursive(start+1, stop)

recusriveResult = sumFromToRecursive(4, 8)
print(recusriveResult)