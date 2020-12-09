class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPosition = nums[-1]
        i = len(nums) - 1 
        while(i >= 0): 
            if i + nums[i] >= lastPosition:
                lastPosition = i 
            i -=1
        return lastPosition == 0 
        