import string
def isDigit(ch):
    return ch in string.punctuation

s=isDigit(".")
print(s)