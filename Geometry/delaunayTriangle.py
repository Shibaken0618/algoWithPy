from triangles import *
import math

delaunay = [pointsToTriangle((0.2,0.8), (0.5,0.2), (0.8,0.7))]
pointToAdd = [0.5,0.5]

invalid_triangles = []
delaunay_index = 0

while delaunay_index < len(delaunay):
    circumcenter, radius = triangleToCircumcenter(delaunay[delaunay_index])
    new_distance = getDistance(circumcenter,pointToAdd)
    if (new_distance < radius):
        invalid_triangles.append(delaunay[delaunay_index])
    delaunay_index += 1

points_in_invalid = []

for i in range(len(invalid_triangles)):
    delaunay.remove(invalid_triangles[i])
    for j in range(0,len(invalid_triangles[i])):
        points_in_invalid.append(invalid_triangles[i][j])
points_in_invalid = [list(x) for x in set(tuple(x) for x in points_in_invalid)]

for i in range(len(points_in_invalid)):
    for j in range(i+1, len(points_in_invalid)):
        count_occurences = 0
        for k in range(len(invalid_triangles)):
            count_occurences += 1 * (points_in_invalid[i] in invalid_triangles[k]) * \
                (points_in_invalid[j] in invalid_triangles[k])
            
        if (count_occurences == 1):
            delaunay.append(pointsToTriangle(points_in_invalid[i], points_in_invalid[j], \
                pointToAdd))

