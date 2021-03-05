# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if(root == None):
            return [0]
        
        q = [root]
        re = []
        while q:
            r = len(q) 
            l = [] 
            for i in range(0, r): 
                c = q.pop(0)
                l.append(c.val)
                if c.left != None: 
                    q.append(c.left)
                if c.right != None:
                    q.append(c.right) 
            re.append(sum(l) / len(l))
        return re 
        
