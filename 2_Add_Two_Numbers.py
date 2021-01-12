# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        base = 1 
        result = 0 
        while(l1 != None):
            result += base * l1.val 
            l1 = l1.next 
            base *= 10 
        base2 = 1 
        result2 = 0 
        while(l2 != None):
            result2 += base2 * l2.val 
            l2 = l2.next 
            base2 *= 10 
        summ = result + result2 
        
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
    
            
