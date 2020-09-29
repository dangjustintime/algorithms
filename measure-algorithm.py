import arrayGenerator
import functools
import resource
import time
import timeit

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print("step " + str(i) + ":\t\t\t" + str(arr))
    return arr

def measureAlgorithm(func, input):
    print("Function:\t\t" + func.__name__ + "()")
    print("Input:\t\t\t" + str(input) + "\n")
    print("\nRun Time:\t\t" + str(timeit.timeit(functools.partial(func, input), number = 1)))
    print("Memory Size:\t\t" + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) + " bytes")
    print("Output:\t\t\t" + str(input))

measureAlgorithm(insertionSort, arrayGenerator.generateArray())
