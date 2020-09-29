import random
import sys

def generateArray(length = 5, smallest = -9, largest = 9, number = 1):
    arr = []
    while len(arr) < number:
        smallArr = []
        while len(smallArr) < length:
            smallArr.append(random.randrange(smallest, largest, 1))
        arr.append(smallArr)
    return arr
