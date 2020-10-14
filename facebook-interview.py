from collections import deque
import random
import arrayGenerator

# definition for a node
class Node(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def insertLevelOrder(arr, rootNode, index):
    if index < len(arr):
        rootNode = Node(arr[index])
        rootNode.left = insertLevelOrder(arr, rootNode.left, 2 * index + 1)
        rootNode.right = insertLevelOrder(arr, rootNode.right, 2 * index + 2)
    return rootNode

# breadth first search
# V = vortex    E = edge
# time complexity: O(|V| + |E|)
# space complexity: O(|V|)
def BFS(rootNode, target):
    # initialize queue
    # push root node in queue
    queue = deque([rootNode])

    # iterate through queue until empty
    while queue:
        # remove element from queue and get value
        numNodes = len(queue)
        node = queue.popleft()
        
        print(node.val)

        # if value equal target, return
        if node.val is target:
            print("**FOUND**")
            return True
        
        for i in range(numNodes):
            # push children to queue
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
    return False

# depth first search
# V = vortex    E = edge
# time complexity: O(|V| + |E|)
# space complexity: O(|V|)
def DFS(rootNode, target):
    print(rootNode.val)
    if rootNode.val is target:
        print("**FOUND**")
        return True
    if rootNode.left:
        DFS(rootNode.left, target)
    if rootNode.right:
        DFS(rootNode.right, target)

# binary search
def BinarySearch(arr, left, right, target):
    print(arr[left:right + 1])
    # check base case
    if right >= left:
        
        # find middle
        mid = 1 + (right - left) // 2

        # if element is target
        if arr[mid] == target:
            return mid
        # select lower half if target < mid
        elif arr[mid] > target:
            return BinarySearch(arr, left, mid - 1, target)
        # select higher half if target > mid
        else:
            return BinarySearch(arr, mid + 1, right, target)

head = insertLevelOrder([1, 2, 3, 4, 5, 6, 7, 8], Node(), 0)

arr = arrayGenerator.generateArray()
BinarySearch(arr, 0, len(arr) - 1, arr[2])
