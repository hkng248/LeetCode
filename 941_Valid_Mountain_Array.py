class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False 
        increasing = True 
        if(arr[0] > arr[1]):
            return False 
        
        for i in range(1, len(arr)):
            if(arr[i] > arr[i-1]) and increasing:
                continue 
            elif(arr[i] == arr[i-1]):
                return False 
            elif(arr[i] < arr[i-1]) and increasing:
                increasing = False 
            elif(arr[i] < arr[i-1] and increasing == False):
                continue 
            elif(arr[i] > arr[i-1] and increasing == False):
                return False
        if(increasing):
            return False 
        return True 
                
                
        