class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        f = {} 
        for j in arr:
            if j in f.keys():
                f[j] += 1 
            else:
                f[j] = 1 
        s = 0 
        max_values = sorted(f.values())
        
        half = len(arr) / 2 
        while(half > 0): 
            half -= max_values.pop() 
            s += 1 
            
        return s 