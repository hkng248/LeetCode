class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "" 
        
        ans = self.computeCommonPrefix(strs)
        if len(ans):
            return ans 
        else:
            return "" 
        
    def computeCommonPrefix(self, strs):
        prefix = strs[0] 
        for i in range(1, len(strs)):
            prefix = self.commonPrefix(prefix, strs[i]) 
        return (prefix) 
    
    def commonPrefix(self, str1, str2): 
        result = "" 
        n1 = len(str1)
        n2 = len(str2)
        i = 0; j = 0 
        while i <= n1 - 1 and j <= n2 - 1:
            if str1[i] != str2[j]:
                break
            result += str1[i] 
            i += 1 
            j += 1 
        return (result) 
        