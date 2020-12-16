class Solution:
    def quicksort(self, nums):
        if len(nums) < 2:
            return nums 
        low, equal, high = [], [], []
        pivot = nums[randint(0, len(nums) - 1)]
        for i in nums:
            if i < pivot:
                low.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                high.append(i)
        return self.quicksort(low) + equal + self.quicksort(high)
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [] 
        for j in nums:
            squares.append(j*j) 
        return self.quicksort(squares)

'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [] 
        for j in nums:
            squares.append(j*j) 
        squares.sort()
        return squares 
'''