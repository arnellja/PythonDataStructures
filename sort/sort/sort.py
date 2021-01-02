import math # used to round.
import random # used to generate random list
from time import * # used for timing the sort functions.
import array # used to create temporary array in quicksort(lyst)
from recursioncounter import RecursionCounter # counts recursive calls in quicksort and mergesort functions.
from test_sort import *

def main():

    ROUND_VALUE = 4 # number of significant figures desired in reported times.
    SEED_VALUE = 42 # seed value for the random generator.
    random.seed(SEED_VALUE) # seeds the random generator.
    startCount = 0.00 # used as start time for all sort functions.
    mergeCount = 0.00 # elapsed time for mergesort
    quickCount = 0.00 # elapsed time for quicksort
    selectionCount = 0.00 # elapsed time for selection_sort
    insertionCount = 0.00 # elapsed time for insertion_sort
    timCount = 0.00 # elapsed time for timsort
    RANGE = 1000000 # defines range of numbers to be put in the list.
    SIZE = 10000 # defines size of list.
    lyst = random.sample(range(RANGE),SIZE) # generates list of random values.
    selectionCopy = lyst.copy() # creates copy of lyst to be used for selection_sort.
    insertionCopy = lyst.copy() # creates copy of lyst to be used for insertion_sort.
    mergeCopy = lyst.copy() # creates copy of lyst to be used for mergesort.
    quickCopy = lyst.copy() # creates copy of lyst to be used for quicksort.
    timCopy = lyst.copy() # creates copy of lyst to be used for timsort.



    print("starting selection_sort")
    startCount = perf_counter() # begin timing for selection_sort.
    selectionCopy = selection_sort(selectionCopy) # calls selection_sort using copy of lyst.
    selectionCount = perf_counter() # end time after selection_sort.
    print("selection_sort duration: ", round(selectionCount - startCount, ROUND_VALUE), " seconds\n") # prints elapsed time during selection_sort.
    
    print("starting insertion_sort")
    startCount = perf_counter() # begin timing for insertion_sort.
    insertionCopy = insertion_sort(insertionCopy) # calls insertion_sort using copy of lyst.
    insertionCount = perf_counter() # end time for insertion_sort.
    print("insertion_sort duration: ", round(insertionCount - startCount, ROUND_VALUE), " seconds\n") # prints elapsed time during insertion_sort.

    print("starting mergesort")
    startCount = perf_counter() # begin timing for mergesort.
    mergeCopy = mergesort(mergeCopy) # calls mergesort using copy of lyst.
    mergeCount = perf_counter() # end time for mergesort.
    print("mergesort duration: ", round(mergeCount - startCount, ROUND_VALUE), " seconds\n") # prints elapsed time during mergesort.

    print("starting quicksort")
    startCount = perf_counter() # begin time for quicksort
    quickCopy = quicksort(quickCopy) # calls quicksort using copy of lyst.
    quickCount = perf_counter() # end time for quicksort.
    print("quicksort duration: ", round(quickCount - startCount, ROUND_VALUE), " seconds\n") # prints elapsed time during quicksort.

    print("starting timsort")
    startCount = perf_counter() # begin time for timsort.
    timCopy = sorted(timCopy) # calls timsort usinig copy of lyst.
    timCount = perf_counter() # end time for timsort.
    print("timsort duration: ", round(timCount - startCount, ROUND_VALUE), " seconds\n") # prints elapsed time during timsort.

    


def selection_sort (lyst): # recieves list of values out of order, and sorts using a selection sort. Returns sorted list.
    if (type(lyst) != list): # raises ValueError if item recieved is not a list.
        raise ValueError("Information provided not a list")
    largeIndex = 0 # index of largest value.
    temp = 0 # used for swapping.
    endMark = len(lyst) # last element that will be considered. As the highest values are swapped to the end, the endMark will decrease.
    counter = 0 # used for iterating the list with the while loop.
    for x in lyst:
        counter = 0
        endMark -= 1 # disregards element at end of list from consideration, which is largest value left in considered list after each iteration.
        while(counter < endMark): # iterates through list and finds greatest value.
            if (lyst[counter] > lyst[largeIndex]):
                largeIndex = counter
            counter += 1
        temp = lyst[largeIndex] # swaps the greatest value in the list with the last considered element.
        lyst[largeIndex] = lyst[endMark]
        lyst[endMark] = temp
    return lyst



def insertion_sort(lyst): # recieves a list of values out of order, and sorts it using a insertion sort. Returns sorted list.
    if (type(lyst) != list): # raises ValueError if item recieved is not a list.
        raise ValueError("Information provided not a list")
    counter = 1 # used for iterating outer while loop.
    counter2 = 1 # used for iterating inner while loop.
    temp = 0 # used for swapping elements in list.
    sortedList = 0 # number of elements that have been sorted in the list.
    while (counter < len(lyst)): # iterates through entire list.
        counter2 = sortedList + 1 # counter2 set as index of value after the sorted portion of list.
        while (counter2 > 0 & counter2 < len(lyst)-1): # sets bounds on what counter2 may be equal to - avoids out of bounds error.
            if (lyst[counter2] < lyst[counter2 - 1]): # checks if item at counter2 is smaller than items preceding it.
                temp = lyst[counter2]  # for every item larger than item at counter2, the elements will swap.
                lyst[counter2] = lyst[counter2 - 1]
                lyst[counter2 - 1] = temp
            counter2 -= 1 # decrements counter2, so as to compare it to its new preceding element.
        sortedList += 1 # amount of sorted elements increases by 1 after each iteration of the outer while loop.
        counter += 1
    return lyst


def quicksort(lyst): # recieves a list of values out of order, and sorts it using a quick sort. Returns sorted list.
    if (type(lyst) != list): # raises ValueError if item recieved is not a list.
        raise ValueError("Information provided not a list")
    return quicksort_helper (lyst, 0, len(lyst) - 1) # calls recursive helper with endpoints of the list.

def quicksort_helper(lyst, lower, higher): # recursive helper for the quick sort.
    RecursionCounter() # counts the number of recursions.
    if (lower < higher): # compares the endpoints provided, checks if they are in order.
        pivot = new_list(lyst, lower, higher) 
        quicksort_helper(lyst, lower, pivot) # recursively calls self using lower endpoint and pivot index.
        quicksort_helper(lyst, pivot + 1, higher) # recursively calls self using pivot index + 1 and higher endpoint.
    return lyst # returns a sorted list if in order.

def new_list(lyst, lower, higher):  # recieves list and endpoints, and then returns a index for an effective pivot.
    midPoint = (lower + higher) // 2 # finds midpoint of list.
    pivot = lyst[midPoint] # sets pivot equal to element at index midpoint, then swaps elements at midpoint and the high bound.
    lyst[midPoint] = lyst[higher]
    lyst[higher] = pivot

    barrier = lower # sets boundary at the lower bound.

    for x in range(lower, higher): # iterates through list and compares each element to pivot.
        if (lyst[x] < pivot): # if value is less than pivot, the value is swapped with the value at the boundary.
            temp = lyst[x]
            lyst[x] = lyst[barrier]
            lyst[barrier] = temp
            barrier += 1 # boundary moves forward after each swapped item.

    temp = lyst[higher] # swaps the elements at high bound and barrier.
    lyst[higher] = lyst[barrier]
    lyst[barrier] = temp
    return barrier # returns new pivot


def mergesort(lyst): # recieves a list of values out of order, and sorts the values using a merge sort. Returns the ordered list.
    if (type(lyst) != list): # raises ValueError if the item recieved is not a list.
        raise ValueError("Information provided not a list")
    emptySpace = array.array('i', range(0, len(lyst))) # creates temporary array to store sorted values during merge.
    return mergesort_helper(lyst, emptySpace, 0, len(lyst) - 1) # calls recursive helper with original list, empty list, and endpoints.

def mergesort_helper(lyst, emptySpace, lower, higher): # recursive helper for merge sort.
    RecursionCounter() # counts number of recursion used by function.
    if (lower < higher): # compares endpoints of list.
        midPoint = (lower + higher) // 2 # finds midpoint index of list.
        mergesort_helper(lyst, emptySpace, lower, midPoint) # recursively calls self using endpoints of lower bound and midpoint.
        mergesort_helper(lyst, emptySpace, midPoint + 1, higher) # recursively calls self using endpoints of midpoint and upper bound.
        combine_lists(lyst, emptySpace, lower, midPoint, higher) # merges the lower half of the list with the upper half.
    return lyst

def combine_lists(lyst, emptySpace, lower, midPoint, higher): # helper for merge sort, used to merge two sorted lists.
    counter1 = lower # sets counter1 to value at lower bound.
    counter2 = midPoint + 1 # sets counter2 to value after midpoint.

    for x in range(lower, higher + 1): # iterates number of times equal to higher + 1 - lower.
        if (counter1 > midPoint): # checks if counter1 is smaller or larger than the front half's upper bound.
            emptySpace[x] = lyst[counter2] # if counter1 is greater than the midPoint, immediately appends contents of upper half to emptySpace.
            counter2 += 1
        elif (counter2 > higher): # checks if counter2 is smaller or larger than the back half's upper bound.
            emptySpace[x] = lyst[counter1] # if counter2 is greater than the upper bound, immediately appends contents of lower half to emptySpace.
            counter1 += 1
        elif (lyst[counter1] < lyst[counter2]): # compares elements in lower half to elements in upper half.
            emptySpace[x] = lyst[counter1] # appends element from lower half to emptySpace if smaller.
            counter1 += 1
        else:
            emptySpace[x] = lyst[counter2] # appends element from upper half to emptySpace if smaller.
            counter2 += 1
    for x in range(lower, higher + 1): # sets element order of lyst equal to the order of ordered emptySpace.
        lyst[x] = emptySpace[x]
    return lyst

def is_sorted(lyst): # this has been checked and works.
    if (type(lyst) != list): # raises ValueError if item recieved is not a list.
        raise ValueError("Information provided not a list")
    x = 0
    while( x < (len(lyst)-1)): # iterates through entire list.
        if (type(lyst[x]) != int): # raises ValueError if any element of list is not an integer.
            raise ValueError("All elements should be integers")
        if (lyst[x] > lyst[x+1]): # returns false if any preceding value is greater than its following value.
            return False
        x += 1
    return True

