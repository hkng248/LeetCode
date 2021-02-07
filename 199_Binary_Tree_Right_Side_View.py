# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        if root == None:
            return result
        
        queue = [root]
        while queue: 
            size = len(queue) 
            level = []
            for i in range(0, size): 
                c = queue.pop(0)
                level.append(c.val) 
                if c.left != None:
                    queue.append(c.left)
                if c.right != None:
                    queue.append(c.right)
            result.append(level[-1])
        return result 