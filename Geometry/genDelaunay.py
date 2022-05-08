from triangles import *

def genDelaunay(points):
    delaunay = [pointsToTriangle([-5,-5],[-5,10],[10,-5])]
    numberOfPoints = 0

    while numberOfPoints < len(points):
        pointToAdd = points[numberOfPoints]
        delaunayIndex = 0
        invalidTriangles = []
        while delaunayIndex < len(delaunay):
            circumcenter,radius = triangleToCircumcenter(delaunay[delaunayIndex])
            newDistance = getDistance(circumcenter,pointToAdd)
            if newDistance < radius:
                invalidTriangles.append(delaunay[delaunayIndex])
            delaunayIndex += 1

        pointsInInvalid = []
        for i in range(0,len(invalidTriangles)):
            delaunay.remove(invalidTriangles[i])
            for j in range(0,len(invalidTriangles[i])):
                pointsInInvalid.append(invalidTriangles[i][j])
        pointsInInvalid = [list(x) for x in set(tuple(x) for x in pointsInInvalid)]

        for i in range(0,len(pointsInInvalid)):
            for j in range(0,i+1, len(pointsInInvalid)):
                countOccurences = 0
                for k in range(0,len(invalidTriangles)):
                    countOccurences += 1 * (pointsInInvalid[i] in invalidTriangles[k]) * \
                        (pointsInInvalid[j] in invalidTriangles[k])
                if countOccurences == 1:
                    delaunay.append(pointsToTriangle(pointsInInvalid[i], \
                        pointsInInvalid[j],pointToAdd))
        
        numberOfPoints += 1
    return delaunay
