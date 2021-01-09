# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        listOfValues = []
        while head != None:
            listOfValues.append(head.val)
            head = head.next 
            
        left = 0
        right = len(listOfValues) - 1 
        while(left < right):
            if(listOfValues[left] != listOfValues[right]):
                return False 
            left += 1 
            right -= 1 
        return True 
        