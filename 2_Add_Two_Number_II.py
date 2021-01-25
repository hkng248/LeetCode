# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modify(self, node):
        base = 1 
        result = 0 
        while(node != None):
            result += base * node.val 
            node = node.next
            base *= 10 
        return result 
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        summ = self.modify(l1) + self.modify(l2) 
        head = None 
        if(summ >= 0): 
            root = ListNode(summ % 10) 
            summ = summ // 10 
            head = root 
            while(summ > 0):
                root.next = ListNode(summ % 10)
                summ = summ // 10 
                root = root.next 
        return head 
    
            
