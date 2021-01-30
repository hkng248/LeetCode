#README: This solution fails a particular test case therefore this solution is void.
#I wanted to add this so that I will remember to revisit this later. 
#This problem is docked as "Hard". 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict 

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if(root == None):
            return []
        queue = [] 
        queue.append(root)
        levelMap = defaultdict(list)
        levelMap[0] = [root.val]
        cLevelMap = {} 
        cLevelMap[root.val] = 0
        while queue: 
            current = queue.pop(0) 
            cLevel  = cLevelMap[current.val]
            if(current.left != None):
                cLevelMap[current.left.val] = cLevel - 1
                levelMap[cLevel - 1].append(current.left.val)
                queue.append(current.left)
            if(current.right != None):
                cLevelMap[current.right.val] = cLevel + 1
                levelMap[cLevel + 1].append(current.right.val) 
                queue.append(current.right)
            for k in levelMap.keys(): 
                levelMap[k].extend(sorted(levelMap[k]))
        result = [] 
        for k in sorted(levelMap.keys()):
            result.append(levelMap[k])
        return result 
                