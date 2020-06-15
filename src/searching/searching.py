def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    first = 0
    middle = len(arr) // 2
    last = len(arr) - 1

    found = False
    # we start by searching the very first value
    while first <= last and not found:
        middle = (first + last) // 2

        if arr[middle] == target:
            found = True
            return middle

        else:
        # if the target is less than the current value
        #  move the middle to the left one, and reset
        # the last value to be the middle minus one
        # cutting our search feild in half
            if arr[middle] > target:
                last = middle - 1

        #if the target is greater than the middle value
        # we reset the first value to be one above the middle value
        #again cutting the search in half
            else:
                first = middle + 1

    return -1  # not found


