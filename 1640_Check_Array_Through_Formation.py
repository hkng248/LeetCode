class Solution(object):
    def canFormArray(self, arr, pieces):
        mapOfKeys = {} 
        for i in pieces:
            mapOfKeys[i[0]] = i 
            
        while arr: 
            current = arr[0]
            if(current in mapOfKeys.keys()): 
                for j in mapOfKeys[current]:
                    current = arr.pop(0)
                    if j != current: 
                        return False 
            else:
                return False 
        return len(arr) == 0 
        