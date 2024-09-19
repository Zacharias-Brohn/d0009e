import math

def derivative(f,x,h):
	return (f(x + h) - f(x - h)) / (2 * h)

def writeDerivative():
	# Exempel 1, f(x) = sin(x), f'(x) = cos(x), x = π / 4
	approxDerivative1 = derivative(math.sin, (math.pi / 4), 1e-5)
	actualDerivative1 = math.cos(math.pi / 4)
	print("f(x) = sin(x) at x = π/4: \nApproximate",f"= {approxDerivative1}\nActual","",f"= {actualDerivative1}",sep="\t")

# Exempel 2, f(x) = x^2, f'(x) = 2x, x = 2
def fexempel(x):
	return x ** 2

def writeDerivative1():
	approxDerivative2 = derivative(fexempel, 2, 1e-5)
	actualDerivative2 = 2 * 2
	print("\nf(x) = x^2 at x = 2: \nApproximate",f"= {approxDerivative2}\nActual","",f"= {actualDerivative2}",sep="\t")

def writeDerivative2():
	# Exempel 3, f(x) = ln(x), f'(x) = 1/x, x = 0.1
	approxDerivative3 = derivative(math.log, 0.1, 1e-5)
	actualDerivative3 = 1 / 0.1
	print("\nf(x) = ln(x) at x = 0.1: \nApproximate",f"= {approxDerivative3}\nActual","",f"= {actualDerivative3}",sep="\t")

def solve(f,x0,h):
	x_n = x0 					# Första gissning
	while True:
		f_xn = f(x_n)			        # Funktionens value vid nuvarande gissning
		f_prime_xn = derivative(f, x_n, h)      # Derivatan vid nuvarande gissning
		if f_prime_xn == 0:					# Undvik att dela med 0
			return
		x_next = x_n - f_xn / f_prime_xn	# Newton-Raphsons metod
		if abs(x_next - x_n) < h:	# Kollar om x har konvergerat
			return x_next
		x_n = x_next				# Ny gissning

def exempel1(x):                # f(x) = x^2 - 1
	return x ** 2 - 1

def exempel2(x):		# f(x) = 2^x - 1
	return 2 ** x - 1

def exempel3(x):		# f(x) = x - e^(-x)
	return x - math.exp(-x)

def solveExempel1_1():
	h = 1e-5
	x0 = 10
	root = solve(exempel1, x0, h)
	print("\nRoot 1 of x^2 - 1 and guess x = 10",f": {root}",sep="\t")
	return
def solveExempel1_2():
	h = 1e-5
	x0 = -10
	root = solve(exempel1, x0, h)
	print("Root 2 of x^2 - 1 and guess x = -10",f": {root}",sep="\t")
	return
def solveExempel2():
	h = 1e-5
	x0 = 5
	root = solve(exempel2, x0, h)
	print("Root of 2^x - 1 and guess x = 5","",f": {root}",sep="\t")
	return
def solveExempel3():
	h = 1e-5
	x0 = 15
	root = solve(exempel3, x0, h)
	print("Root of x - e^(-x) and guess x = 15",f": {root}",sep="\t")
	return

