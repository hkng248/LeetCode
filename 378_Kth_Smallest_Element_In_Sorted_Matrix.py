class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(sum(matrix, []))[k-1]
    
#         listOfNumbers = [] 
#         if matrix: 
#             findRow = len(matrix[0]) 
#             if k < findRow: 
#                 return matrix[0][k-1]
#             else: 
#                 while(k > len(matrix[0])): 
#                     matrix.pop(0)
#                     k -= len(matrix[0])
#                 return matrix[0][k-1]
#         return -1 