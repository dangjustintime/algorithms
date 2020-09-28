import resource
import time

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def measureAlgorithm(func, input):
    startTime = time.time_ns();
    output = func(input)
    endTime = time.time_ns();
    runTime = endTime - startTime;
    print("\n------------------------------------------------------------\n")
    print("Function:\t\t" + func.__name__ + "()")
    print("Input:\t\t" + str(input))
    print("Output:\t\t" + str(output))
    print("Run Time:\t\t" + str(runTime) + " seconds")
    print("Memory Size:\t\t" +str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) + " bytes")
    print("\n------------------------------------------------------------\n")

measureAlgorithm(insertionSort, [3, 5, 0, 6])
