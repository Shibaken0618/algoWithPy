from sortedBinarySearch import binarySearch
import math

def inverseSin(number):
 domain = [x * math.pi/10000 - math.pi/2 for x in list(range(0,10000))]
 the_range = [math.sin(x) for x in domain]
 result = domain[binarySearch(the_range,number)]
 return(result)

arcSin = inverseSin(0.9)
print(arcSin)