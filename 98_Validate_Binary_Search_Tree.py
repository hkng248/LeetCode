# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validateTree(root, None, None) 
    
    def validateTree(self, root, low, high):
        if(root == None):
            return True 
        
        if((low != None and low >= root.val) or (high != None and high <= root.val)):
            return False 
        return self.validateTree(root.left, low, root.val) and self.validateTree(root.right, root.val, high)
        