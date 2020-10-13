from collections import deque

# definition for a node
class Node(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# breadth first search
# V = vortex    E = edge
# time complexity: O(|V| + |E|)
# space complexity: O(|V|)
def BFS(rootNode, target):
    # initialize queue
    # push root node in queue
    queue = deque(rootNode)

    while queue:
        # pop queue and get value
        node = queue.popleft()

        # return value if node is equal to target
        if node.val == target:
            return node

        # push children to queue
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return -1







