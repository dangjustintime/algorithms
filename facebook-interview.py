from collections import deque
import random

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

head = insertLevelOrder([1, 2, 3, 4, 5, 6, 7, 8], Node(), 0)

