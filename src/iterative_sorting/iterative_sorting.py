def quick_sort(sequence):

    length = len(sequence)

    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()  # removes and returns the last element

    items_greater = [] # list that holds items greater than pivot
    items_lower = [] # list that holds items less than pivot

    # now we do a comparison on each of items left in the sequence to our pivot point
    for item in sequence: # for every item left in our sequence
        print('pivot: ' + str(pivot))
        if item > pivot: # if the item is greater than the pivot point
            items_greater.append(item) # append the item to the list that is greater than
        else:
            items_lower.append(item) # also includes the items that are equal

    # now, what we need to do is apply this algorithm over and over to each of the sub lists that we create
    # we'll do this with a return statement.  ie, a return should apply this algorithm again to each of the
    # of the items lower, we should have that pivot point in the center and we apply the algorithm again
    # the return statement concatenates lists (pivot is put into a list for concat purpuses)
    print(str(items_lower) + ' | ' + str(pivot) + ' | ' + str(items_greater))
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

arr = [0, 9, 3, 8, 2, 7, 5]

print(quick_sort(arr))





# =======================================================================
# =======================================================================
# =======================================================================
# =======================================================================




# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):                               # define buble_sort function that take arr(ay) as an argument
    n = len(arr)                                    # get n (the length of arr, so you know how many times to loop)
    indexing_length = n - 1                         # indexing length is 1 less of the arr, as no numbers remain to compare
                                                    
    sorted = False                                  # keep track of when sorted is done, True

    while not sorted:                               # keep looping until sorted = True
        sorted = True                               # once the loop stops, sorted is True, as no False was set
        for i in range(0, indexing_length):         # for i at position 0, 1, 2, ..., n-1
            if arr[i] > arr[i+1]:                   # if arr left element is greater than the one on the right
                sorted = False                      # set sorted to False
                arr[i], arr[i+1] = arr[i+1], arr[i] # swap the elements
                print(str(i + 1) + '. ' + str(arr)) # print the swap

    return arr

arr = [63, 5, 11, 22, 17, 3, 1, 5, 88, 92]

bubble_sort(arr)

print(bubble_sort(arr))

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
