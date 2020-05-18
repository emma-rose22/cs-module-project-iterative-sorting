#binary search tree and sorting are related
# -- bst enforces sorting
# -- that same concept can be applied to arrays
# ---- searching based off a midpoint cuts the array in half, similar to BST

#this assumes the array is sorted
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


#insertion sorting example

# we start with two halves, the sorted and unsorted side
# at first, just one value is in the sorted,
# then new elements get added in one by one, being put in 
# the appropriate spot

class Book:
    def __init__(self, title, author, genre)
    self.title = title
    self.author = author
    self.genre = genre

def insertion_sort_books(arr_of_books):
    #what should we sort by? chose title
    for i in range(1, len(arr_of_books)):
        curr_book = arr_of_books[i]
        # put curr_book in the appropriate spot in sorted half
        # loop through sorted half to find appr spot
        j = i
        while j > 0 and curr_book.title < arr_of_books[j-1].title:
            #slide the curr_book over
            # j-1th book and copying it to the jth spot
            arr_of_books[j] = arr_of_books[j-1]
            j -= 1 

        #insert the book at the correct position
        arr_of_books[j] = curr_book
        
    return arr_of_books

#optimized code of the same thing 

def insertion_sort_books(arr_of_books):
    for i in range(1, len(arr_of_books)):
        curr_book = arr_of_books[i]
        j = i
​
        while j > 0 and curr_book.title < arr_of_books[j - 1].title:
            arr_of_books[j], arr_of_books[j - 1] = arr_of_books[j - 1], arr_of_books[j]
            j -= 1
​
    return arr_of_books



'''
Determining time complexity:
​
1. Compute the big O of each line in isolation.
2. If something is in a loop, multiply its big O by the number of iterations of the loop
3. If two things happen sequentially, add the big Os.
4. Drop leading multiplicative constants from each big O.
5. From all the Big-Os that are added, drop all but the biggest, dominating one.
'''
​
​
​
'''
Space (or memory) complexity measures how much _additional_ memory an 
algorithm allocates in order to run.
​
One big giveaway that an algorithm is utilizing additional memory is 
if it initializes a data structure. 
​
We use the same big O notation when talking about space complexity.
​
Just like with time complexity, space complexity is concerned with the worst case. 
'''
​
# O(n) time, O(1) space 
def o_1_space(n):
    total = 0  # O(1)
​
    # range returns a `range` 
    # does the range object utilize a constant amount of space?
    # range takes up a constant amount of space 
    for i in range(n): # O(1) space 
        total += i  # O(1)
​
    return total 
​
​
# O(n) time, O(n) space 
def o_n_space(n):
    sums = []
​
    for i in range(n):
        sums.append(i + i)  # O(n)
​
    return sums
​
​
# O(n^2) time, O(n^2) space
def o_n2_space(n):
    times_table = []
​
    for i in range(n):  # O(n) time 
        row = []
​
        for j in range(n):  # O(n) time
            row.append(j * i)  # we're adding n elements to the `row` list; O(n) space 
​
        times_table.append(row)  # we have n lists that each hold n elements 
​
    return times_table  # O(n^2)
​
​
​
# O(n^2) space
def o_2_space_v2(n):
    times_table = []
​
    for i in range(n):
        times_table.append(i)
​
        for j in range(n):
            times_table.append(j)
​
    return times_table
​
​
​
# space complexity cares about how much _additional_ space is being used 
# O(1) space 
# don't count data structures that are passed in as input 
def foo(arr):
    for x in arr:
        print(x + x)
​
​
​
# O(n) space 
def bar(arr):
    output = []
​
    for n in arr:
        output.append(n * n)  # O(n) space 
​
    return output
​
​
# arr is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# O(n)
def baz(arr):
    evens = []
​
    # we're adding half of the values from the input array 
    for n in arr:
        if n % 2 == 0:
            evens.append(n) # O(n / 2) == O(1/2 * n) ~ O(n) space 
​
    return evens
​
​
​
# Pass by reference: the function is receiving a pointer to the input 
