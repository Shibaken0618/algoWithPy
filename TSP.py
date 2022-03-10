from code import InteractiveInterpreter
import numpy as np
import math

randomSeed = 1729
np.random.seed(randomSeed)
N = 40
x = np.random.rand(N)
y = np.random.rand(N)
print(x)
print(y)
points = zip(x,y)
print(points)
cities = list(points)
print(cities)
itinerary = list(range(0,N))
print(itinerary)

lines = []
for j in range(0,len(itinerary)-1):
    lines.append([cities[itinerary[j]], cities[itinerary[j+1]]])

def genlines(cities,itinerary):
    lines = []
    for j in range(0,len(itinerary)-1):
        lines.append([cities[itinerary[j]],cities[itinerary[j+1]]])
    return lines

lines = genlines(cities,itinerary)
print(lines)

def howFar(lines):
    distance = 0
    for j in range(len(lines)):
        distance += math.sqrt(abs(lines[j][1][0] - lines[j][0][0])**2 + \
        abs(lines[j][1][1]-lines[j][0][1])**2)
    return distance

distance = howFar(lines)
print(distance)

import matplotlib.collections as mc
import matplotlib.pylab as pl

def plotItinerary(cities,itin,plottitle,thename):
    lc = mc.LineCollection(genlines(cities,itin),linewidths=2)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    pl.scatter(x,y)
    pl.title(plottitle)
    pl.xlabel('X Coordinate')
    pl.ylabel('Y Coordinate')
    pl.savefig(str(thename))
    pl.close()


plotItinerary(cities,itinerary,'TSP-Random Itinerary','figure')