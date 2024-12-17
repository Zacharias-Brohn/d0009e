def sumRec(lst): # recursive implementation
  if len(lst)==0:
    return 0 # identity element for addition
  return lst[0]+sumRec(lst[1:])

def sumIter(lst): # iterative implementation
  i=0
  sum=0
  while i<len(lst):
    sum += lst[i]
    i +=1
  return sum

def selectLargest(lstlst):
  largestIndex=0
  largestSum=sumRec(lstlst[0])
  i=1 # we start at one, since we already computed sum for index 0 above
  while i<len(lstlst):
    currentSum = sumRec(lstlst[i])
    if currentSum > largestSum:
      largestSum   = currentSum
      largestIndex = i
    i +=1
  return lstlst[largestIndex]
