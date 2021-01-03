# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == None:
            return None    
        queue = []
        queue.append(cloned) 
        while queue: 
            n = len(queue) 
            root = queue.pop() 
            if root.val == target.val:
                return root
            if root.left != None:
                queue.append(root.left)
            if root.right != None:
                queue.append(root.right) 
        return None 
                
                
        