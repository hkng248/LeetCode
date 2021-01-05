# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        listOfValues = [] 
        while(l1 != None): 
            listOfValues.append(l1.val)
            l1 = l1.next 
        while(l2 != None):
            listOfValues.append(l2.val)
            l2 = l2.next 
        listOfValues = sorted(listOfValues) 
        if len(listOfValues) == 0:
            return None 
        
        root = ListNode(listOfValues.pop(0))
        head = root 
        for j in listOfValues:
            root.next = ListNode(j)
            root = root.next 
        return head 
                

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = None 
        if(l1 == None and l2 == None):
            return None 
        if(l1 == None and l2 != None):
            return l2 
        if(l1 != None and l2 == None):
            return l1
        
        if l1.val < l2.val: 
            root = ListNode(l1.val) 
            l1 = l1.next 
        else:
            root = ListNode(l2.val) 
            l2 = l2.next 
        
        head = root 
        while(l1 != None and l2 != None):
            if l1.val > l2.val:
                root.next = ListNode(l2.val) 
                l2 = l2.next 
            else:
                root.next = ListNode(l1.val)
                l1 = l1.next 
            root = root.next 
        
        while(l1 != None): 
            root.next = ListNode(l1.val)
            l1 = l1.next 
            root = root.next 
        while(l2 != None):
            root.next = ListNode(l2.val)
            l2 = l2.next
            root = root.next 
            
        return head 
                
'''