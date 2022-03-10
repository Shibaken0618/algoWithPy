from code import InteractiveInterpreter
from TSP import genlines, howFar, plotItinerary
import numpy as np
import math
import matplotlib.collections as mc
import matplotlib.pylab as pl

randomSeed = 1729
np.random.seed(randomSeed)
N = 40
x = np.random.rand(N)
y = np.random.rand(N)
points = zip(x,y)
cities = list(points)
itinerary = list(range(0,N))


def findNearest(cities,idx,nnitinerary):
    point = cities[idx]
    mindistance = float('inf')
    minidx = -1
    for j in range(0,len(cities)):
        distance = math.sqrt((point[0] - cities[j][0])**2 + (point[1] - cities[j][1])**2)
        if distance < mindistance and distance > 0 and j not in nnitinerary:
            mindistance = distance
            minidx = j
    return minidx

def donn(cities,N):
    nnitinerary = [0]
    for j in range(0,N-1):
        next = findNearest(cities,nnitinerary[len(nnitinerary) - 1],nnitinerary)
        nnitinerary.append(next)
    return nnitinerary


plotItinerary(cities,donn(cities,N),'TSP - Nearest Neighbor','figure2')
print(howFar(genlines(cities,donn(cities,N))))
