from mergeSort import mergesort, merging
from sortedBinarySearch import binarySearch

cabinet = [4,1,3,2,6,3,18,2,9,7,3,1,2.5,-9]


def mergeSortBinarySearch(cabinet,lookingFor):
    newcabinet = mergesort(cabinet)
    return binarySearch(newcabinet,lookingFor)
    

whereNumber = mergeSortBinarySearch(cabinet,2.5)
print(whereNumber)