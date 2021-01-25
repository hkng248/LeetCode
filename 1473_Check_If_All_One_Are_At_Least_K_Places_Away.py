class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = -1
        for i in range(0, len(nums)): 
            if nums[i] == 1: 
                if last != -1:
                    if(i - last <= k):
                        return False 
                last = i 
        return True 
    
            
