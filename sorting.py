# Recitation 10 - Sorting
# Don't forget you can ask the course staff or your recitation partner if you have any questions regarding this activity


from timeit import timeit
from random import randrange

#   All of the coding for this assignment will be in these three functions

def selection_sort(numList):
    """Selection Sort: choose first, second, etc."""
    size = len(numList)
    for pos in range(size):
        minpos = pos
        for seek in range(pos,size):    # find smallest in range
            # -- YOUR CODE STARTS HERE
            if (numList[seek] <= numList[minpos]):
                minpos = seek
            # -- YOUR CODE ENDS HERE


        numList[minpos],numList[pos] = numList[pos],numList[minpos]

def insertion_sort(numList):
    """Insertion Sort: insert each new element into sorted array"""
    size = len(numList)
    for pos in range(1,size):
        value = numList[pos]              # insert this value into sorted data
        # -- YOUR CODE STARTS HERE
        #When inserting the value, repeatedly swap the value from its current position
        #to its correct position, thus performing an insertion
        for x in range(pos-1, -1, -1):
            if (numList[x] >= value):
                numList[x], numList[x+1] = numList[x+1], numList[x]
                pos -= 1
            else:
                break
        
        # -- YOUR CODE ENDS HERE
        numList[pos] = value 



def bubble_sort(numList):
    """Bubble Sort: exchange any adjacent values that are out of order"""
    size = len(numList)
    sorted = False                      # expect to check at least once
    while not sorted:
        sorted = True                   # assume it is sorted this time
        for pos in range(1,size):
            if numList[pos] < numList[pos-1]:
                # -- YOUR CODE STARTS HERE
                numList[pos-1], numList[pos] = numList[pos], numList[pos-1]
                sorted = False
                # -- YOUR CODE ENDS HERE




# Functions to test the results quickly

def verify(numList):
    """Make sure the data is sorted"""
    size = len(numList)
    for pos in range(1,size):
        if numList[pos] < numList[pos-1]:
            print("Not sorted at positions", pos-1, "and", pos)
            return False
    return True

def test_sort():
    """Test sorts for ten element array"""
    arr = [1,3,5,7,9,8,6,4,2,0]
    selection_sort(arr)
    print(f'arr after Selection sort: {arr}')
    
    arr = [1,3,5,7,9,8,6,4,2,0]
    insertion_sort(arr)
    print(f'arr after Insertion sort: {arr}')
    
    arr = [1,3,5,7,9,8,6,4,2,0]
    bubble_sort(arr)
    print(f'arr after Bubble sort: {arr}')


def time_test(sort,size=0):
    """Time these sorts for a given array size"""
    arr = [0]*size
    for i in range(size):
        arr[i] = randrange(1000000000)
    time1 = timeit('sort(arr)', globals = locals(), number=1)
    time2 = timeit('sort(arr)', globals = locals(), number=1)
    print("{:7.3f} s".format(time1),"{:7.3f} s".format(time2)) 
    verify(arr)


test_sort()
print(f'Selection Sort')
time_test(selection_sort, 500)
time_test(selection_sort, 1000)
print(f'Insertion Sort')
time_test(insertion_sort, 500)
time_test(insertion_sort, 1000)

print(f'Bubble Sort')
time_test(bubble_sort, 500)
time_test(bubble_sort, 1000)

#   This is a bad approximation of the bubble sort, for demonstration only
    
def bad_sort(numList):
    size = len(numList)
    i = 1
    while i < size:
        if numList[i] < numList[i-1]:
            numList[i],numList[i-1] = numList[i-1],numList[i]
            i = 1
        else:
            i = i+1
print(f'Bad Sort: ')
time_test(bad_sort,50) 
time_test(bad_sort,100)
time_test(bad_sort,200)
