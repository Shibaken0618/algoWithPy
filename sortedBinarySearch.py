import math

def binarySearch(cabinet,lookingFor):
    guess = math.floor(len(cabinet)/2)
    upperBound = len(cabinet)
    lowerBound = 0
    while(abs(cabinet[guess] - lookingFor) > 0.0001):
        if lookingFor > cabinet[guess]:
            lowerBound = guess
            guess = math.floor((guess + upperBound)/2)
        elif lookingFor < cabinet[guess]:
            upperBound = guess
            guess = math.floor((guess + lowerBound)/2)
    return guess


# cabinet = [1,2,3,4,5,6,7,8,9]
# print(binarySearch(cabinet,8))

