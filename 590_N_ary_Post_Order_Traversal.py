"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        return self.postorderHelper(root, [])
    
    def postorderHelper(self, root, values):
        if(root == None):
            return values
        
        if(root.children != None):
            for i in root.children:
                values = self.postorderHelper(i, values)
        values.append(root.val)
        return values
                
        