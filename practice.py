#I saw some code for the binary search algorithim in passing
#good practice for the brain to try to recreate it!
#it is the Olog(n) recursive approach

def where_is_it(dataset, value):
    #we need to cut our list in half
    # midpoint, low, high

    low = 0
    highpoint = len(dataset) - 1
    midpoint = (highpoint - low) // 2

    print(midpoint)
    print(dataset)
    print('stop?')

    #return the value if the midpoint equals it

    if dataset[midpoint] == value:
        return midpoint

    #narrow the search down to the half of the data our value should be in
    #if midpoint >= low:
    if value < dataset[midpoint]:
        dataset = dataset[:midpoint]
        print('It is less than the midpoint')
        #return where_is_it(dataset, value)
    if value > dataset[midpoint]:
        print('It is greater than the midpoint')
        dataset = dataset[midpoint:]
        #return where_is_it(dataset, value)

    #if the midpoint reaches zero, something is wrong or the value isn't here
    # else:
    #     return print('Item not in list')
    # repeat the process until the midpoint equals our value
    where_is_it(dataset, value)



test = [1,2,3,4,5,6,7,8,9,10]

where_is_it(test, 8)


# whiteboard = ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]

# for i in whiteboard:
#     print(i)


w2 = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

def unpackw2(arr):
    for i in arr:
        if type(i) is list:
            unpackw2(i)
        else:
            print(i)


#unpackw2(w2)