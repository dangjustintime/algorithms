from collections import deque
import arrayGenerator
import random
import sys

# helper functions
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

def generateSinglyLinkedList(arr):
    head = Node(arr[0])
    currentNode = head
    for i in range(1, len(arr)):
        nextNode = Node(arr[i])
        currentNode.right = nextNode
        currentNode = nextNode
    return head

def printSinglyLinkedList(head):
    string = ""
    while head:
        string += "{} -> ".format(head.val)
        head = head.right
    print(string)

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
    visited = {}
    return DFSUtil(rootNode, target, visited)

def DFSUtil(rootNode, target, visited):
    if not rootNode or rootNode in visited:
        return False
    print(rootNode.val)
    visited[rootNode] = True
    if rootNode.val is target:
        return True
    return DFSUtil(rootNode.left, target, visited) or DFSUtil(rootNode.right, target, visited)

# binary search
# time complexity: O(log n)
# space complexity: O(1)
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

# matching parenthese
# time complexity: O(n)
# space complexity: O(n)
def matchingParenthesis(string):
    # initialize stack
    stack = deque([])

    # iterate through string
    for i in range(len(string)):
        char = string[i]
        
        # check if open parenthesis
        if char == "(" or char == "[" or char == "{":
            # add to stack if open parenthesis
            stack.append(char)
        # check if closed parenthesis
        elif char == ")" or char == "]" or char == "}":
            # return false if stack is empty
            if not stack:
                return False

            # pop stack
            top = stack.pop();

            # return false if top of stack does not match
            if char == ")" and top != "(":
                return False
            elif char == "]" and top != "[":
                return False
            elif char == "}" and top != "{":
                return False

    # return true if stack is empty
    return len(stack) == 0

# reverse linked list
# time complexity: O(n)
# space complexity: O(1)
def reverseSinglyLinkedList(head):
    # declare previous node and current node variable
    prevNode = None
    currentNode = head

    # iterate through list
    while currentNode:

        # assign next node to current node next
        nextNode = currentNode.right

        # ***** REVERSE DIRECTION *****
        # assign current node next to previous node
        currentNode.right = prevNode
        
        # assign previous node to current node
        prevNode = currentNode
        
        # assign current node to next node
        currentNode = nextNode
        if not currentNode:
            return prevNode

# tree traversals
# inorder tree traversal
# left, root, right
# time complexity: O(n)
# space complexity: O(1)
def inorderTreeTraversal(rootNode):
    if rootNode:
        inorderTreeTraversal(root.left)
        print(rootNode.val)
        inorderTreeTraversal(root.right)

# postorder tree traversal
# left, right, root
# time complexity: O(n)
# space complexity: O(1)
def postorderTreeTraversal(rootNode):
    if rootNode:
        postorderTreeTraversal(root.left)
        postorderTreeTraversal(root.right)
        print(rootNode.val)

# preorder tree traversal
# root, left, right
# time complexity: O(n)
# space complexity: O(1)
def preorderTreeTraversal(rootNode):
    if rootNode:
        print(root.val)
        preorderTreeTraversal(root.left)
        preorderTreeTraversal(root.right)

root = insertLevelOrder([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], Node(), 0)
print(DFS(root, 999))
