class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1Map ={} 
        for i in nums1: 
            if i in nums1Map.keys():
                nums1Map[i] += 1 
            else:
                nums1Map[i] = 1 
        for j in nums2:
            if j in nums1Map.keys():
                if nums1Map[j] > 0:
                    nums1Map[j] -= 1 
                    result.append(j) 
                else:
                    pass 
        return result 
        