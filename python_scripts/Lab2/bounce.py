def bounce(n):
    # Skriv nuvarande nummer
    print(n)

    # Om n=0 avslutas funktion
    if n == 0:
        return

    # Rekursiv nedräkning
    bounce(n - 1)

    # Pga. python funk. stack skriv upp från 0
    print(n)

def bounce2(n):
    # Loop räknar ned från n till 0
    for i in range(n, -1, -1):
        print(i)
    
    # Loop räknar upp från 0 till n
    for i in range(1, n + 1):
        print(i)

def tvarsumman(n):
    if n < 0:
        print("needs positive value")
        return
    if n == 0:
        return 0
    else:
        # Rekursiv funktion där sista numret adderas till rest nummer
        return n % 10 + tvarsumman(n // 10)

def tvarsumman2(n):
    total = 0
    if n < 0:
        return
    # Loop tills n är 0
    while n > 0:
        # Addera sista nummer till total variabel
        total += n % 10
        
        # Ta bort sista nummer från n
        n //= 10
    
    return total
