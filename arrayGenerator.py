import random

def generateArray(length = 5, smallest = -9, largest = 9, number = 1):
    arr = []
    while len(arr) < length:
        arr.append(random.randrange(smallest, largest, 1))
    return arr
