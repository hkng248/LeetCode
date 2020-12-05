"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        return self.preorderHelper(root, [])
    
    def preorderHelper(self, root, values): 
        if root == None:
            return values 
        values.append(root.val)
        if root.children != None:
            for i in root.children:
                values = self.preorderHelper(i, values)
        return values 
        