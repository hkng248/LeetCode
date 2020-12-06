"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if(root == None):
            return 
        #Breadth first search 
        queue = []
        queue.append(root) 
        levels = [] 
        head = root 
        while queue: 
            size = len(queue) 
            level = []
            for i in range(0, size):
                node = queue.pop(0)
                level.append(node)
                if(node.left != None):
                    queue.append(node.left)
                if(node.right != None):
                    queue.append(node.right)
            levels.append(level) 
        #Iterate through the nodes and create assign pointers 
        for level in levels:
            size = len(level)
            count = 1
            for node in level:
                if node == level[-1] or count >= len(level):
                    node.next = None
                else:
                    node.next = level[count]
                count += 1
        return head
        
        
        