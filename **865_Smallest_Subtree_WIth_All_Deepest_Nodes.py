#ReDO this problem. 

#LeetCode solutions
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        # The result of a subtree is:
        # Result.node: the largest depth node that is equal to or
        #              an ancestor of all the deepest nodes of this subtree.
        # Result.dist: the number of nodes in the path from the root
        #              of this subtree, to the deepest node in this subtree.
        Result = collections.namedtuple("Result", ("node", "dist"))
        def dfs(node):
            # Return the result of the subtree at this node.
            if not node: return Result(None, 0)
            L, R = dfs(node.left), dfs(node.right)
            if L.dist > R.dist: return Result(L.node, L.dist + 1)
            if L.dist < R.dist: return Result(R.node, R.dist + 1)
            return Result(node, L.dist + 1)

        return dfs(root).node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
#         if root == None:
#             return []
#         queue = []
#         queue.append(root)
#         result = [] 
#         while queue:
#             level = [] 
#             size = len(queue)
#             for i in range(size):
#                 node = queue.pop(0)
#                 level.append(node)
#                 if node.left != None:
#                     queue.append(node.left)
#                 if node.right != None:
#                     queue.append(node.right)
#             result.append(level) 
#         if(len(result) == 1):
#             return root 
        
#         currentMin = float('inf')
#         minn = root
#         if(len(result[-1]) == 1):
#             return result[-1][0]
        
#         for j in result[-2]:
#             if(currentMin > j.val) and j.left != None and j.right != None:
#                 currentMin = min(currentMin, j.val)
#                 minn = j
#         return minn 
        
        
        