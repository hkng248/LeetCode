# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        listOfRoutes = self.calculateRoutes(root, [], "")
        count = 0
        for j in listOfRoutes:
            if(self.canFormPalindrome(j)):
                count += 1 
        return count 
        
    def calculateRoutes(self, root, listOfRoutes, currentPath): 
        if root == None:
            listOfRoutes.append(currentPath)
            return listOfRoutes 
        
        currentPath += str(root.val) 
        if(root.left != None):
            listOfRoutes = self.calculateRoutes(root.left, listOfRoutes, currentPath) 
        if(root.right != None):
            listOfRoutes = self.calculateRoutes(root.right, listOfRoutes, currentPath)
        if(root.left == None and root.right == None):
            listOfRoutes.append(currentPath)
        return listOfRoutes 
        
    def canFormPalindrome(self, string):
        count = [0] * 256 
        for i in range(0, len(string)):
            count[ord(string[i])] = count[ord(string[i])] + 1 
        odd = 0 
        for i in range(0, 256):
            if(count[i] & 1):
                odd = odd + 1 
            if odd > 1:
                return False 
        return True 