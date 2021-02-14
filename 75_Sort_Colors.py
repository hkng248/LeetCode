class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = {0:0, 1:0, 2:0}
        for i in nums:
            count[i] += 1 
        z = 0
        for j in range(3):
            for k in range(count[j]):
                nums[z], z = j, z + 1 
        return nums 
        



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        hashMap = {} 
        for j in nums:
            if j in hashMap.keys():
                hashMap[j] += 1 
            else:
                hashMap[j] = 1 
        
        index = 0; result = [0,1,2]
        for k in result: 
            if k in hashMap.keys():
                for i in range(hashMap[k]):
                    nums[index] = k 
                    index += 1 
        return nums 
        