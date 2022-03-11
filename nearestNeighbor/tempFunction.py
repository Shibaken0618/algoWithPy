import matplotlib.pyplot as plt
import numpy as np
import math
from TSP import howFar,genlines

temperature = lambda t:1/(t+1)
ts = list(range(0,100))
plt.plot(ts,[temperature(t) for t in ts])
plt.title('The Temperature Function')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.show()

def perturb_sa1(cities,itinerary,time):
    neighborids1 = math.floor(np.random.rand()*(len(itinerary)))
    neighborids2 = math.floor(np.random.rand()*(len(itinerary)))

    itinerary2 = itinerary.copy()
    itinerary2[neighborids1] = itinerary[neighborids2]
    itinerary2[neighborids2] = itinerary[neighborids1]

    distance1 = howFar(genlines(cities,itinerary))
    distance2 = howFar(genlines(cities,itinerary2))

    itineraryToReturn = itinerary.copy()

    randomdraw = np.random.rand()
    temperature = 1/((time/1000) + 1)

    if ((distance2 > distance1 and (randomdraw) < (temperature)) or (distance1 > distance2)):
        itineraryToReturn = itinerary2.copy()

    return itineraryToReturn.copy()

itinerary = [i for i in range(0,40)]
randomSeed = 1729
N = 40
x = np.random.rand(N)
y = np.random.rand(N)
points = zip(x,y)
cities = list(points)
np.random.seed(randomSeed)
itinerary_sa = itinerary.copy()
for n in range(0,len(itinerary)*50000):
    itinerary_sa = perturb_sa1(cities,itinerary_sa,n)

# print(howFar(genlines(cities,itinerary_sa)))


def perturb_sa2(cities,itinerary,time):
    neighborids1 = math.floor(np.random.rand()*(len(itinerary)))
    neighborids2 = math.floor(np.random.rand()*(len(itinerary)))

    itinerary2 = itinerary.copy()
    randomdraw2 = np.random.rand()
    small = min(neighborids1,neighborids2)
    big = max(neighborids1,neighborids2)
    if randomdraw2 >= 0.55:
        itinerary2[small:big] = itinerary2[small:big][::-1]
    elif randomdraw2 < 0.45:
        tempitin = itinerary[small:big]
        del(itinerary2[small:big])
        neighborids3 = math.floor(np.random.rand()*(len(itinerary)))
        for j in range(0,len(tempitin)):
            itinerary2.insert(neighborids3 + j,tempitin[j])
    else:
        itinerary2[neighborids1] = itinerary[neighborids2]
        itinerary2[neighborids2] = itinerary[neighborids1]

    distance1 = howFar(genlines(cities,itinerary)) 
    distance2 = howFar(genlines(cities,itinerary2)) 

    itineraryToReturn = itinerary.copy()
    randomdraw = np.random.rand()
    temperature = 1/((time/1000) + 1)

    scale = 3.5
    if((distance2 > distance1 and (randomdraw) < (math.exp(scale*(distance1-distance2))*
    temperature)) or (distance1 > distance2)):
        itineraryToReturn = itinerary2.copy()
    
    return itineraryToReturn.copyy()
