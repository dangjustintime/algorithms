import arrayGenerator
import functools
import resource
import sort
import timeit

"""
    measure algorithm
"""
def measureAlgorithm(func, input):
    print("Function:\t\t" + func.__name__ + "()")
    print("Input:\t\t\t" + str(input) + "\n")
    print("\nRun Time:\t\t" + str(timeit.timeit(functools.partial(func, input), number = 1)))
    print("Memory Size:\t\t" + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) + " bytes")
    print("Output:\t\t\t" + str(input))

measureAlgorithm(sort.mergeSort, arrayGenerator.generateArray())
