"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


''' Iterative solution using a queue '''
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if(root == None):
            return [] 
        
        queue = [] 
        queue.append(root)
        result = [] 
        while queue: 
            size = len(queue)
            level = []
            for i in range(0, size):
                node = queue.pop(0)
                level.append(node.val)
                if node.children:
                    for i in node.children:
                        queue.append(i) 
            result.append(level)
        return result 

''' Recursive solution ''' 
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = self.levelOrderTraversal(root, {}, 0)
        result = [] 
        for level in levels.values(): 
            result.append(level)
        return result 
    
    
    def levelOrderTraversal(self, root, levels, level): 
        if(root == None):
            return levels
        if level in levels.keys(): 
            levels[level].append(root.val) 
        else:
            levels[level] = [root.val] 
        
        if root.children:
            for i in root.children: 
                levels = self.levelOrderTraversal(i, levels, level +1)
        return levels 
        