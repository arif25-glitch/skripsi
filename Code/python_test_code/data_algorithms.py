import pandas as pd
import numpy as np
import time

def fibonacci(value1=0, value2=1, stop_loop=5):
    if stop_loop <= 0:
        return
    print(value1)
    fibonacci(value2, (value1 + value2), stop_loop=stop_loop-1)

def nFib(n):
    return n if n <= 1 else nFib(n - 1) + nFib(n - 2)

def bubble_sort(my_array):
    n = len(my_array)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
                swapped = True
        if not swapped:
            break
    return my_array

# quicksort
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

def insertion_sort(my_array):
    n = len(my_array)
    for i in range(1,n):
        insert_index = i
        current_value = my_array[i]
        for j in range(i-1, -1, -1):
            if my_array[j] > current_value:
                my_array[j+1] = my_array[j]
                insert_index = j
            else:
                break
        my_array[insert_index] = current_value

def selectionSort(value):
    for i in range(len(value)):
        minimum_index = i
        for j in range(i+1, len(value)):
            if value[j] < value[minimum_index]:
                minimum_index = j
        value[i], value[minimum_index] = value[minimum_index], value[i]
    return value

def linearMinMaxArray(value):
    min = value[0]; max = value[0]
    for i in range(1, len(value)):
        if value[i] <= min:
            min = value[i]
        if value[i] >= max:
            max = value[i]
    return min, max, (sum(value) / len(value))

if __name__ == "__main__":
    startTime = time.time()
    
    a = [np.random.randint(-10000, 10000) for i in range(1000000)] 
    # for i in range(len(a)):
    #     for j in range(i):
    #         if a[i] < a[j]:
    #             a[i], a[j] = a[j], a[i]
    
    quicksort(a)
    print(round(time.time() - startTime, 5))
    
    # fibonacci(stop_loop=12)
    # fibonacci(stop_loop=10)
    
    # min, max, mean = linearMinMaxArray([np.random.randint(0, 1000) for i in range(100)])
    # print(f'Minimum: {min}, Maximum: {max} Mean: {mean}')