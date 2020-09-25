import resource
import timeit

def helloWorld():
    print("Hello World")

print("Run Time:\t\t" + str(timeit.timeit("helloWorld()", number=1, globals=globals())) + " seconds")
print("Memory Size:\t\t" +str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) + " bytes")
