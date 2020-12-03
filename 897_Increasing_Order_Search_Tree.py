# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        values = self.inorder(root, [])
        newRoot = TreeNode(values.pop(0)) 
        head = newRoot
        while values:
            newRoot.right = TreeNode(values.pop(0))
            newRoot = newRoot.right 
        return head
        
        
    def inorder(self, root, values): 
        if(root == None):
            return values 
        if root.left != None:
            values = self.inorder(root.left, values) 
        values.append(root.val)
        if root.right != None:
            vales = self.inorder(root.right, values) 
        return values 

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        values = self.BFS(root)
        values.sort()
        
        newRoot = TreeNode(values.pop(0))
        head = newRoot
        while values:
            newRoot.right = TreeNode(values.pop(0))
            newRoot = newRoot.right 
        return head
        
        
    def BFS(self, root): 
        if(root == None):
            return []
        values = []
        queue = [root] 
        while queue: 
            size = len(queue) 
            curr = queue.pop(0) 
            values.append(curr.val)
            if curr.left != None: 
                queue.append(curr.left)
            if curr.right != None:
                queue.append(curr.right) 
        return values 
'''