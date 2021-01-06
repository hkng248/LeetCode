# I need to review Linked Lists. This code solution is not very good 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        setOfValidNumbers = set() 
        bannedSet = set() 
        while(head != None):
            if(head.val in bannedSet):
                pass 
            elif(head.val in setOfValidNumbers): 
                setOfValidNumbers.remove(head.val) 
                bannedSet.add(head.val) 
            else:
                setOfValidNumbers.add(head.val) 
            head = head.next 
            
        validNumbers = sorted(list(setOfValidNumbers))
        root = None 
        if len(validNumbers) > 0: 
            root = ListNode(validNumbers.pop(0))
        head = root 
        for j in validNumbers:
            root.next = ListNode(j) 
            root = root.next 
        return head 
            
        
