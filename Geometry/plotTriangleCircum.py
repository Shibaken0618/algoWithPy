from matplotlib.pyplot import subplot, xscale
from pkg_resources import yield_lines

import pylab as pl
import math
from matplotlib import collections as mc
from triangles import *
from genDelaunay import genDelaunay


def plotTriangleCircum(triangles,centers,plotcircles,plotpoints,plottriangles,plotvoronoi,plotvpoints,thename):
    fig, ax = pl.subplot 
    ax.set_xlim([-0.1,1.1])
    ax.set_ylim([-0.1,1.1])

    lines = []
    for i in range(0,len(triangles)):
        triangle = triangles[i]
        center = centers[i][0]
        radius = centers[i][1]
        itin = [0,1,2,0]
        thelines = genLines(triangle,itin)
        xs = [triangle[0][0],triangle[1][0],triangle[2][0]]
        ys = [triangle[0][1],triangle[1][1],triangle[2][1]]

        lc = mc.LineCollection(genLines(triangle,itin), linewidths=2)
        if plottriangles:
            ax.add_collection(lc)
        if plotpoints:
            pl.scatter(xs,ys)
        ax.margins(0.1)
        if plotvpoints:
            pl.scatter(center[0],center[1])
        circle = pl.Circle(center,radius,color='b',fill = False)
        if plotcircles:
            ax.add_artist(circle)
        if plotvoronoi:
            for j in range(0,len(triangles)):
                commonpoints = 0
                for k in range(0,len(triangles)):
                    for n in range(0,len(triangles[i])):
                        if triangles[i][k] == triangles[j][n]:
                            commonpoints += 1
                if commonpoints == 2:
                    lines.append([list(centers[i][0]),list(centers[j][0])])
        lc = mc.LineCollection(lines,linewidths = 1)
        ax.add_collection(lc)

    pl.savefig(str(thename) + '.png')
    pl.close()