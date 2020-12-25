class Solution:
    def firstUniqChar(self, s: str) -> int:
        charMap = {} 
        for i in s:
            if i in charMap.keys(): 
                charMap[i] += 1 
            else:
                charMap[i] = 1 
        for key, value in charMap.items():
            if value == 1:
                return s.index(key)
        return -1 
        