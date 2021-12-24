# selection sort (sort from smallest to largest)
# 1. find the location with smallest element in array
# 2. pop that element while appending to new array
# 3. continue process till all elements in initial array gone

def findSmallest(arr):
    smallest = arr[0]
    smallestLocation = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestLocation = i
    return smallestLocation

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


# sort from largest to smallest (one function)
def selectionSort2(arr):
    newArr = []
    for i in range(len(arr)):
        largest = arr[0]
        largestLocation = 0
        for k in range(len(arr)):
            if arr[k] > largest:
                largest = arr[k]
                largestLocation = k
        newArr.append(arr.pop(largestLocation))
    return newArr


# test
print(selectionSort([5,4,2,1,3]) == [1,2,3,4,5])
print(selectionSort2([8,10,9,6,7]) == [10,9,8,7,6])
