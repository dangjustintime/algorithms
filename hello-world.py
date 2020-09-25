import resource
import timeit

def helloWorld():
    print("Hello World")

def measureAlgorithm(func):
    print("\n------------------------------------------------------------\n")
    print("Function:\t\t" + helloWorld.__name__ + "()")
    print("Run Time:\t\t" + str(timeit.timeit(func.__name__, number=1, globals=globals())) + " seconds")
    print("Memory Size:\t\t" +str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) + " bytes")
    print("\n------------------------------------------------------------\n")

measureAlgorithm(helloWorld)
