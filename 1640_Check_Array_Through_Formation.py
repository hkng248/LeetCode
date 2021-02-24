class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        keys = {} 
        for piece in pieces:
            keys[piece[0]] = piece 
        while arr: 
            piece = arr[0] 
            if piece in keys.keys():
                for i in keys[piece]:
                    if i != arr.pop(0):
                        return False 
            else:
                return False 
                
        return len(arr) == 0
            
        