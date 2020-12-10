# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    Node = None 
    listOfValues = None 

    def __init__(self, root: TreeNode):
        self.Node = root 
        self.listOfValues = self.traverseTree(root, [])
    
    def traverseTree(self, root, listOfValues):
        if(root == None):
            return listOfValues 
        #in-order (left - root -right) 
        if(root.left != None):
            listOfValues = self.traverseTree(root.left, listOfValues)
        listOfValues.append(root.val)
        if(root.right != None):
            listOfValues = self.traverseTree(root.right, listOfValues)
        return listOfValues
        

    def next(self) -> int:
        return self.listOfValues.pop(0)
        

    def hasNext(self) -> bool:
        return len(self.listOfValues) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()