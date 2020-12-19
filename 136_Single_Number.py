class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = 0 
        for i in set(nums):
            total += i*2 
        return total - sum(nums) 
        