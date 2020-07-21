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
            print('items greater than pivot: ' + str(items_greater))
        else:
            items_lower.append(item) # also includes the items that are equal
            print('items less than pivot: ' + str(items_lower))

    # now, what we need to do is apply this algorithm over and over to each of the sub lists that we create
    # we'll do this with a return statement.  ie, a return should apply this algorithm again to each of the
    # of the items lower, we should have that pivot point in the center and we apply the algorithm again
    # to the items greater. the length of sequence shortens every time; this process repeats until sequence is >= 1
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

arr = [0, 9, 3, 8, 2, 7, 5]

print(quick_sort(arr))