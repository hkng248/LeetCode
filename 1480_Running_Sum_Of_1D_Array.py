class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        for i,j in enumerate(nums[1:], 1): 
            nums[i] = j + nums[i-1]
        return nums