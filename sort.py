"""
    insertion sort
    time complexity: O(n^2)
"""
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

"""
    merge sort
    time complexity: O(n * log(n))
"""
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = mergeSort(arr[:mid]), mergeSort(arr[mid:])
    return merge(left, right, arr.copy())

"""
    merge
"""
def merge(left, right, arr):
    leftCursor, rightCursor = 0, 0
    while leftCursor < len(left) and rightCursor < len(right):
        if left[leftCursor] <= right[rightCursor]:
            arr[leftCursor + rightCursor] = left[leftCursor]
            leftCursor += 1
        else:
            arr[leftCursor + rightCursor] = right[rightCursor]
            rightCursor += 1
    for leftCursor in range(leftCursor, len(left)):
        arr[leftCursor + rightCursor] = left[leftCursor]
    for rightCursor in range(rightCursor, len(right)):
        arr[leftCursor + rightCursor] = right[rightCursor]
    print("Left: {}\tRight: {}\tArray: {}".format(left, right, arr))
    return arr


