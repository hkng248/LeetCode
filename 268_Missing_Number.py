class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        e = len(nums) * (len(nums) + 1) // 2 
        a = sum(nums)
        return e - a 
        