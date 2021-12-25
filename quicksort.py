# function for quicksort using C&Q and recursion

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else: 
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]) == [2, 3, 5, 10])
print(quicksort([5, 76, 234, 543, 43, 4, 1, 9, 3450, 7, 1243]) == [1, 4, 5, 7, 9, 43, 76, 234, 543, 1243, 3450])