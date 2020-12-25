class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        tmp = {}
        levels = self.maxDepthHelper(root, tmp, 0) 
        return len(levels.keys())
    
    def maxDepthHelper(self, root, levels, level):
        if root == None:
            return levels 
        if level in levels.keys():
            levels[level].append(root.val) 
        else:
            levels[level] = [root.val]
            
        if(root.left != None):
            levels = self.maxDepthHelper(root.left, levels, level + 1) 
        if(root.right != None):
            levels = self.maxDepthHelper(root.right, levels, level + 1) 
        return levels 
            