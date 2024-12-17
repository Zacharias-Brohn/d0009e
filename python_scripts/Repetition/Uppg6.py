def lst():
    lst1 = [6, 3, 7, 1, 2, 3]
    lst2 = [4, 8, 4, 9, 1, 3]
    lstlst = [lst1, lst2]
    sumR1 = sumRec(lst1)
    sumR2 = sumRec(lst2)
    sumI1 = sumIter(lst1)
    sumI2 = sumIter(lst2)
    print(f"Recursive, list 1: {sumR1}, list 2: {sumR2}")
    print(f"Iterative, list 1: {sumI1}, list 2: {sumI2}")
    largest_list = selectLargest(lstlst)
    print(largest_list)

def sumRec(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sumRec(lst[1:])

def sumIter(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

def selectLargest(lstlst):
    max_sum = sumIter(lstlst[0])
    largest_list = None
    for i in lstlst:
        current_sum = sumIter(i)
        if current_sum > max_sum:
            max_sum = current_sum
            largest_list = i
    return largest_list

lst()