import math

def continuedFraction(x,y,lengthTolerance):
    output = []
    big = max(x,y)
    small = min(x,y)
    while small > 0 and len(output) < lengthTolerance:
        quotient = math.floor(big/small)
        output.append(quotient)
        new_small = big%small
        big = small
        small = new_small
    return(output)

conFrac = continuedFraction(105,33,10)
print(conFrac)

def getNumber(continuedFraction):
    index = -1
    number = continuedFraction[index]
    while abs(index) < len(continuedFraction):
        next = continuedFraction[index-1]
        number = 1/number + next
        index -= 1
    return number

print(getNumber(conFrac))
print(105/33)