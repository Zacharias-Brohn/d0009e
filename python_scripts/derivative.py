import math

def derivative(f,x,h):
	return (f(x+h)-f(x-h))/(2*h)

# Exempel 1, f(x) = sin(x), f'(x) = cos(x)
approxDerivative1 = derivative(math.sin,(math.pi/4),1e-5)
actualDerivative1 = math.cos(math.pi/4)
print("f(x) = sin(x) at x = π/4: \nApproximate",f"= {approxDerivative1}\nActual","",f"= {actualDerivative1}",sep="\t")

# Exempel 2, f(x) = x^2, f'(x) = 2x
def square(x):
	return x ** 2
approxDerivative2 = derivative(square,2,1e-5)
actualDerivative2 = 2 * 2
print("\nf(x) = x^2 at x = 2: \nApproximate",f"= {approxDerivative2}\nActual","",f"= {actualDerivative2}",sep="\t")

# Exempel 3, f(x) = ln(x), f'(x) = 1/x
approxDerivative3 = derivative(math.log,0.1,1e-5)
actualDerivative3 = 1 / 0.1
print("\nf(x) = ln(x) at x = 0.1: \nApproximate",f"= {approxDerivative3}\nActual","",f"= {actualDerivative3}",sep="\t")

def solve(f,x0,h):
	x=x0
	tolerance=1e-7
	while True:
		f_x = f(x)
		f_prime_x = derivative(f, x, h)
		if f_prime_x == 0:
			print("Derivative is zero. No solution found.")
			return None
		x_new = x - f_x / f_prime_x
		if abs(x_new - x) < tolerance:
			print(f"Converged to root: {x_new}")
			return x_new
		x = x_new