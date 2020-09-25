def helloWorld():
    print("Hello World")

import timeit

print("Run Time: " + str(timeit.timeit("helloWorld()", number=1, globals=globals())) + " seconds")

