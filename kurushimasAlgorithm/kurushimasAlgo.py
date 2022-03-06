import math
from rules import *
import random
from fillSquare import *

n = 7
center_i = math.floor(n/2)
center_j = math.floor(n/2)

square = [[float('nan') for i in range(0,n)] for j in range(0,n)]
square[center_i][center_j] = int((n**2 + 1)/2)
square[center_i + 1][center_j] = 1
square[center_i - 1][center_j] = n**2
square[center_i][center_j + 1] = n**2 + 1 - n
square[center_i][center_j - 1] = n

entry_i = center_i
entry_j = center_j

square = fillSquare(square,entry_i,entry_j,(n**2)/2 - 4)
entry_i = math.floor(n/2) + 1
entry_j = math.floor(n/2)
square = fillSquare(square,entry_i,entry_j,0)

square = [[n**2 if x == 0 else x for x in row] for row in square]

print(square)

