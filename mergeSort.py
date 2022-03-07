import math

# when merging two sorted lists together
def merging(left,right):
    newcabinet = []
    while(len(left) > 0 and len(right) > 0):
        if left[0] > right[0]:
            to_insert = right.pop(0)
            newcabinet.append(to_insert)
        elif left[0] <= right[0]:
            to_insert = left.pop(0)
            newcabinet.append(to_insert)
    if(len(left) > 0):
        for i in left:
            newcabinet.append(i)
    if(len(right)>0):
        for i in right:
            newcabinet.append(i)
    return(newcabinet)


left = [1,3,4,4,5,7,8,9]
right = [2,4,6,7,8,8,10,12,13,14]
newcab=merging(left,right)
print(newcab)


def mergesort(cabinet):
    newcabinet = []
    if(len(cabinet) == 1):
        newcabinet = cabinet
    else:
        halfpoint = math.floor(len(cabinet)/2)
        left = mergesort(cabinet[:halfpoint])
        right = mergesort(cabinet[halfpoint:])
        newcabinet = merging(left,right)
    return newcabinet

cabinet = [4,1,3,2,6,3,18,2,9,7,3,1,2.5,-9]
newcabinet = mergesort(cabinet)
print(newcabinet)

