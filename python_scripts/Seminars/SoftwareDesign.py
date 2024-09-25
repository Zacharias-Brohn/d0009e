import math

# All of the comments accomplish the same thing as final func when uncommented
def dis(x1,y1,x2,y2):
    # dx       = (x2-x1)
    # dy       = (y2-y1)
    # dsquared = dx*dx + dy*dy
    # result   = math.sqrt(dsquared)
    # xy12squared = (x2-x1)**2 + (y2-y1)**2
    # result      = math.sqrt(xy12squared)
    # result = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    # return result
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
	
#========================================================

def isDivisible(x,y):
	# if x%y == 0:
	#	return True
	# else:
	#	return False
	return (x%y) == 0

#========================================================
	
def printBool():	
	# if isDivisible(x,y) == True:
	#	print("x is divisible by y")
	# else:
	#	print("x isn't divisible by y")
	
	if isDivisible(x,y):
		print("x is divisible by y")
	else:
		print("x isn't divisible by y")

#========================================================

def printRow(n,a):
	i=1
	while i <= a:
		print(n*i,'\t',end="")
		i=i+1
	print()
	return

def printTable(a):
	i=1
	while i <= a:
		printRow(i,i)
		i=i+1
	return
printTable(8)

#def printTable(a):
#	i=1
#	while i <= a:
#		printRow(i,a)
#		i=i+1
#	return


