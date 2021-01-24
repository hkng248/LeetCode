# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        mapOfValues = {} 
        for j in lists:
            while(j != None): 
                if j.val in mapOfValues: 
                    mapOfValues[j.val] += 1 
                else:
                    mapOfValues[j.val] = 1 
                j = j.next 
            
        keysSort = sorted(mapOfValues.keys()) 
        root = None 
        head = None 
        for j in keysSort: 
            while(mapOfValues[j] > 0):
                if root == None: 
                    root = ListNode(j)
                    head = root 
                else:
                    root.next = ListNode(j) 
                    root = root.next 
                mapOfValues[j] -= 1 
        return head 
                    
                
        
