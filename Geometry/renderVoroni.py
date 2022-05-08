import numpy as np
from triangles import *
from genDelaunay import genDelaunay
from plotTriangleCircum import plotTriangleCircum


N = 15
np.random.seed(5201314)
xs = np.random.rand(N)
ys = np.random.rand(N)
points = zip(xs,ys)
listpoints = list(points)
the_delaunay = genDelaunay(listpoints)

circumcenters = []
for i in range(0,len(the_delaunay)):
    circumcenters.append(triangleToCircumcenter(the_delaunay[i]))
    plotTriangleCircum(the_delaunay,circumcenters,True,True,True,True,True,'everything')
    