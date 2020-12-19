class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        tmp = nums[::-1]
        k %= len(nums)
        tmp = tmp[k-1::-1] + tmp[:k-1:-1]
        index = 0 
        for i in tmp:
            nums[index] = i 
            index += 1 

        


