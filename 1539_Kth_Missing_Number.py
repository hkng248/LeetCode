class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        numberSet = set(arr)
        index = 1 
        while True:
            if index not in numberSet:
                 k -= 1
            if k == 0:
                return index 
            index += 1 
        return -1
        
