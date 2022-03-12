import pylab as pl
import math
from matplotlib import collections as mc

def pointsToTriangle(p1,p2,p3):
    triangle = [list(p1),list(p2),list(p3)]
    return triangle

def genLines(listpoints,itinerary):
    lines = []
    for j in range(0,len(itinerary)-1):
        lines.append([listpoints[itinerary[j]],listpoints[itinerary[j+1]]])
    return lines

def plotTriangleSimple(triangle,thename):
    fig, ax = pl.subplots()
    xs = [triangle[0][0],triangle[1][0],triangle[2][0]]
    ys = [triangle[0][1],triangle[1][1],triangle[2][1]]

    itin = [0,1,2,0]
    theLines = genLines(triangle,itin)
    lc = mc.LineCollection(genLines(triangle,itin), linewidth = 2)
    ax.add_collection(lc)

    ax.margins(0.1)
    pl.scatter(xs,ys)
    pl.savefig(str(thename))
    pl.close()

def getDistance(point1,point2):
    distance = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    return distance

triangle = pointsToTriangle((0.2,0.8),(0.5,0.2),(0.8,0.7))
plotTriangleSimple(triangle,'tri')

def triangleToCircumcenter(triangle):
    x = complex(triangle[0][0],triangle[0][1])
    y = complex(triangle[1][0],triangle[1][1])
    z = complex(triangle[2][0],triangle[2][1])
    w = z-x
    w /= y-x
    c = (x-y) * (w-abs(w)**2)/2j/w.imag-x
    radius = abs(c+x)
    return((0-c.real,0-c.imag),radius)

def plotTriangle(triangles,centers,radii,thename):
    fig, ax = pl.subplots()
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    for i in range(0,len(triangles)):
        triangle = triangles[i]
        center = centers[i]
        radius = radii[i]
        itin = [0,1,2,0]
        thelines = genLines(triangle,itin)
        xs = [triangle[0][0],triangle[1][0],triangle[2][0]]
        ys = [triangle[0][1],triangle[1][1],triangle[2][1]]
        lc = mc.LineCollection(genLines(triangle,itin),linewidths=2)

        ax.add_collection(lc)
        ax.margins(0.1)
        pl.scatter(xs,ys)
        pl.scatter(center[0],center[1])

        circle = pl.Circle(center,radius,color='b',fill=False)

        ax.add_artist(circle)
    pl.savefig(str(thename))
    pl.close()

triangle1 = pointsToTriangle((0.1,0.1),(0.3,0.6),(0.5,0.2))
center1, radius1 = triangleToCircumcenter(triangle1)
triangle2 = pointsToTriangle((0.8,0.1),(0.7,0.5),(0.8,0.9))
center2, radius2 = triangleToCircumcenter(triangle2)
plotTriangle([triangle1,triangle2],[center1,center2],[radius1,radius2],'two')

