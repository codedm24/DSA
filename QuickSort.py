#Quick sort algorithm

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    logging.debug(f"pivot: {pivot}, low: {low}, high: {high}")

    for j in range(low,high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    logging.debug(f"array: {array}")
    return i + 1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        logging.debug(f"pivot_index: {pivot_index}")
        logging.debug(f"Sorting left part of pivot")
        quicksort(array, low, pivot_index - 1)
        logging.debug(f"Sorting right part of pivot")
        quicksort(array, pivot_index + 1, high)

array1 = [64,34,25,12,22,11,90,5]
quicksort(array1)
logging.info(f"Sorted array: {array1}")