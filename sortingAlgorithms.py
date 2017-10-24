import random

def random_sort():
    sorts = []
    sorts.append(bubble_sort)
    sorts.append(merge_sort)
    sorts.append(selection_sort)
    sorts.append(shell_sort)
    return random.choice(sorts)

def bubble_sort(items):
    """ Implementation of bubble sort """
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]     # Swap!
                yield # on every item write

# New indexing function that includes the right index.
def get_partial_list(origin_list, left_index, right_index): # Added
    return origin_list[left_index:right_index+1]


def MERGE(A,start,mid,end):
    L = get_partial_list(A,start,mid)
    R = get_partial_list(A,mid+1,end)
    i = 0
    j = 0
    k = start
    for l in range(k,end+1):            # changed
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            A[l] = L[i]
            i = i + 1
        else:
            A[l] = R[j]
            j = j + 1  
        yield

def merge_sort(A,p=0,r=-1):
    if r < 0:
        r = len(A)-1
    if r - p > 0:                          # changed
        mid = int((p+r)/2)
        yield from merge_sort(A,p,mid)
        yield from merge_sort(A,mid+1,r)             # changed
        yield from MERGE(A,p,mid,r)

def selection_sort(collection):
    length = len(collection)
    for i in range(length):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k
                yield
        collection[least], collection[i] = (collection[i], collection[least])

        

def shell_sort(collection):
    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        while i < len(collection):
            temp = collection[i]
            j = i
            while j >= gap and collection[j - gap] > temp:
                collection[j] = collection[j - gap]
                j -= gap
                yield
            collection[j] = temp
            i += 1
