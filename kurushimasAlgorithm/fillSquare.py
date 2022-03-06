import math
from rules import *
import random

def fillSquare(square,entry_i,entry_j,howfull):
    while(sum(math.isnan(i) for row in square for i in row) > howfull):
        whereCanWeGO = []
        n = len(square)
        if(entry_i < (n-1) and entry_j < (n-1)):
            whereCanWeGO.append("down_right")
        if(entry_i < (n-1) and entry_j > 0):
            whereCanWeGO.append("down_left")
        if(entry_i > 0 and entry_j < (n-1)):
            whereCanWeGO.append("up_right")
        if(entry_i > 0 and entry_j > 0):
            whereCanWeGO.append("up_left")

        whereToGo = random.choice(whereCanWeGO)

        if (whereToGo == "upright"):
            new_entry_i = entry_i - 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j],n,True)

        if (whereToGo == "downleft"):
            new_entry_i = entry_i + 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j],n,False)

        if (whereToGo == "upleft"):
            new_entry_i = entry_i - 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j],n,True)

        if (whereToGo == "downright"):
            new_entry_i = entry_i + 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j],n,False)

        if (whereToGo == 'upleft' and (entry_i + entry_j) == (n)):
            new_entry_i = entry_i - 1
            new_entry_j = entry_j - 1
            square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j],n,True)

        if (whereToGo == 'downright' and (entry_i + entry_j) == (n-2)):
            new_entry_i = entry_i + 1
            new_entry_j = entry_j + 1
            square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j],n,False)
        
        entry_i = new_entry_i
        entry_j = new_entry_j
        
    return(square)