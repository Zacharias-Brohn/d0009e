def multTabellIterative(num, sec):
    for i in range(0, sec):
        print(f"{num*(i+1)}")
    
x = int(input("Skriv in ett nummer: "))
y = int(input("Skriv in ett sluttal: "))
multTabellIterative(x, y)

def multTabellRecursive(num, sec):
    if sec == 0:
        return 0
    else:
        multTabellRecursive(num, sec-1)
        numsec = num * sec
        print(numsec)

multTabellRecursive(x, y)