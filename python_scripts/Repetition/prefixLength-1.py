# count and return number of characters c in s
# c is assumed to be one character
def prefixLength(s1,s2):
  i=0
  count=0
  while i<len(s1) and i<len(s2):
    if s1[i]==s2[i]:
      count+=1
    i+=1
  return count
