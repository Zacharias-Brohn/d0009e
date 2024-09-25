def strToInt(str):
    toInt = 0
    n = 0
    for i in str:
        toInt += (ord(i) - ord('0')) * (10 ** ((len(str)-1)-n))
        n += 1
    return toInt
s=strToInt("7034")
print(s)