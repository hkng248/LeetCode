class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = collections.defaultdict(int) 
        ret = 0 
        for t in time:
            if t % 60 == 0: 
                ret += remainders[0] 
            else:
                ret += remainders[60 - (t % 60)]
            remainders[t%60] += 1 
        return ret 
    
# Time Limit Exceeded (brute force solution)   
# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         result = 0 
#         for i in range(0, len(time)):
#             for j in range(i + 1, len(time)):
#                 duration = int(time[i] + time[j])
#                 if(duration % 60 == 0):
#                     result += 1 
#         return result 
    
        