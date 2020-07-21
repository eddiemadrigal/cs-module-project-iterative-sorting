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