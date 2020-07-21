arr1 = [1, 5, 8, 4]

for i in range(len(arr1)):

    min_idx = i
    for j in range(i + 1, len(arr1)):
        if arr1[min_idx] > arr1[j]:
            min_idx = j

    arr1[i], arr1[min_idx] = arr1[min_idx], arr1[i]

print("Sorted Array")
for i in range(len(arr1)):
    print("%d" %arr1[i])





# =======================================================================
# =======================================================================
# =======================================================================
# =======================================================================




# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):                               # define buble_sort function that take arr(ay) as an argument
    n = len(arr)                                    # get n (the length of arr, so you know how many times to loop)
    indexing_length = n - 1                         # indexing link of where we are going to make these comparisons
                                                    # n - 1 because there is no number after to compare
    sorted = False                                  # keep track of when sorted is done, True

    while not sorted:                               # keep looping until sorted = True
        sorted = True
        for i in range(0, indexing_length):         # loop for comparison
            if arr[i] > arr[i+1]:                   # if arr left element is greater than the one on the right
                sorted = False                      # sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i] # swap the elements. when complete, the sorted = False won't activate

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
