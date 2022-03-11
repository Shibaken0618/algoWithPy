import math
import numpy as np
from TSP import howFar, genlines

def perturb(cities,itinerary):
    neighborids1 = math.floor(np.random.rand()*(len(itinerary)))
    neighborids2 = math.floor(np.random.rand()*(len(itinerary)))

    itinerary2 = itinerary.copy()
    itinerary2[neighborids1] = itinerary[neighborids2]
    itinerary2[neighborids2] = itinerary[neighborids1]

    distance1 = howFar(genlines(cities,itinerary))
    distance2 = howFar(genlines(cities,itinerary2))

    itineraryToReturn = itinerary.copy()

    if (distance1 > distance2):
        itineraryToReturn = itinerary2.copy()
    
    return (itineraryToReturn.copy())

randomSeed = 1729
np.random.seed(randomSeed)
N = 40
x = np.random.rand(N)
y = np.random.rand(N)
points = zip(x,y)
cities = list(points)
itinerary = list(range(0,N))
itineraryPs = itinerary.copy()
for n in range(0,len(itinerary)*50000):
    itineraryPs = perturb(cities,itineraryPs)

print(howFar(genlines(cities,itineraryPs)))