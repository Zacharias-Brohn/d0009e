def calcInterestLoan(loan, rate, years):
    
    # Konvertera procent ränta till decimal
    #rate_decimal = rate / 100
    
    # Räkna ränta
    interest = (years+1)*loan*rate/2
    
    # Räkna total kostnad av lån
    totalOwed = loan + interest

    
    return totalOwed

def convertToInt(number):
    if number.is_integer():  # Kollar om det finns decimaler
        return int(number)  # Konvertera till int
    return number  

loan = float(input("Skriv hur mycket som ska lånas: "))  # Input för lån
rate = float(input("Skriv räntan (i %): "))  # Input för ränta
years = float(input("Skriv tidsperioden (i år): "))  # Input för tidsperiod

loan = convertToInt(loan)
rate = convertToInt(rate)
years = convertToInt(years)

totalOwed = calcInterestLoan(loan, rate, years)
totalOwed = convertToInt(totalOwed)

print(f"\nDen totala kostnaden efter {years} år: {totalOwed} kr.")
