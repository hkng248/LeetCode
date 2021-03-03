class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numMap = set()
        total = len(nums)*( len(nums) + 1) // 2 
        left = 0; right = len(nums)-1 
        while(left <= right):
            if nums[left] in numMap:
                return [nums[left], total - (sum(nums) -nums[left])]
            numMap.add(nums[left])
                
            if nums[right] in numMap:
                return [nums[right], total - (sum(nums) - nums[right])]
            numMap.add(nums[right])
                
            left += 1
            right -= 1
        
        