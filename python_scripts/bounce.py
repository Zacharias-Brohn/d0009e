0 till n
    for i in range(1, n + 1):
        print(i)

def tvarsumman(n):
    if n == 0:
        return 0
    else:
        # Rekursiv funktion där sista numret adderas till rest nummer
        return n % 10 + tvarsumman(n // 10)

def tvarsumman2(n):
    total = 0
    
    # Loop tills n är 0
    while n > 0:
        # Addera sista nummer till total variabel
        total += n % 10
        
        # Ta bort sista nummer från n
        n //= 10
    
    return total
