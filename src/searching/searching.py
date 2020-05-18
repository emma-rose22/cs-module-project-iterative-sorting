def linear_search(arr, target):
    # Your code here
    for i in arr:
        if i == target:
            return arr.index(i)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # find the midpoint

    left = 0
    right = len(arr) -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        #check to see on right or left side of target
        if arr[mid] < target:
            arr = arr[:mid]
            #update our 'left' index
            #we can leave behind the midpoint, it didn't match
            left = mid + 1

        else: #if array is greater than target
            arr = arr[mid:]
            right = mid - 1
    #if element doesnt exist
    return -1