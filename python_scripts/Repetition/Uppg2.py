def printTable(num, sec):
    numsec = num*sec
    print(f"{numsec}")

def main():
    num = int(input("Vilket nummer: "))
    sec = int(input("Vilken rad: "))
    printTable(num, sec)

main()