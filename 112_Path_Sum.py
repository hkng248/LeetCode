# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        paths = self.hasPath(root, 0, [])
        if paths:
            return sum in paths
        else:
            return False 
  
    def hasPath(self, root, total, paths):
        if(root == None):
            return False 
        total += root.val 
        if(root.left != None):
            paths = self.hasPath(root.left, total, paths)
        if(root.right != None):
            paths = self.hasPath(root.right, total, paths) 
        if(root.left == None and root.right == None):
            paths.append(total) 
        return paths 
        