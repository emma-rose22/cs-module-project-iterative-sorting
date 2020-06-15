# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
  
        #notes from tk
        # assume index 0 is smallest value
        # begin by looking for the smallest value
        # swap it with index 0
        # update index to be index 1 
        # do this until the index we are looking at is the last index

        #assume index 0 is smallest value
        cur_index = i
        smallest_index = cur_index

        #look for the smallest value
        for x in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[x]:
                smallest_index = x

        print('before switch:', arr[i], arr[smallest_index])

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        cur_index += 1
        print('I just flipped the switch:', arr[i], arr[smallest_index])
        print('arr:', arr)
        print()

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    #repeat until there are no more swaps
    swap = 1

    while swap > 0:
        swap = 0
        for i in range(len(arr) -1):
            # if the card on right is smaller than left
            if arr[i + 1] < arr[i]:
                #swap
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # repeat until there are no more swaps
                swap += 1

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr


numbers = [2, 4, 3, 5, 8 , 7, 1]

#print(selection_sort(numbers))

print(bubble_sort(numbers))