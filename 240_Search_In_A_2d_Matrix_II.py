class Solution:
    
    def binarySearch(self, l, r , row, target):
        if( l >= r):
            return False 
        mid = (l + r ) // 2
        if(row[mid] == target):
            return True
        if(row[mid] < target):
            return self.binarySearch(mid + 1, r, row, target)
        else:
            return self.binarySearch(l, mid, row, target)
        
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        for row in matrix:
            if self.binarySearch(0, len(row), row, target):
                return True 
        return False 