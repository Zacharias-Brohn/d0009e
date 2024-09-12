import math

def derivative(f,x,h):
	return (1/2*h)*((f(x+h))-(f(x-h)))

a=derivative(math.sin,math.pi,0.0001)
b=derivative(math.sin,math.pi,(-0.0001))
c=derivative(math.sin,math.pi,0.0002)
print(a)
print(b)
print(c)