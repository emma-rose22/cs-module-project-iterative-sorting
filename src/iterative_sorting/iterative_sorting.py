# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for x in range(i+1, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x
            # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        #print(f'This index {cur_index}, with this number {arr[cur_index]},')
        #print(f'is greater than this index {smallest_index} with this number {arr[smallest_index]}')


    return arr

#arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
#print(selection_sort(arr1))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swaps = 1
    while swaps > 0:
        swaps = 0
        for i in range(0, len(arr) -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i +1] = arr[i + 1], arr[i]
                swaps += 1

    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(bubble_sort(arr1))

# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
