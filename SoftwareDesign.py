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

v=dis(1,2,4,6)
print(v)