'''
Pseudo Code:
    Create 1 array (iterate left to right) 
    Calculate left max 
    Create 1 array (iterate right to left)
    Calculate right max 
    Create minHeight array (min(leftMax, rightMax)) 
    Iterate through Height:
        if height < minHeight: 
            water += minHeight - height 
        else:
            water = 0 

Time Complexity O(n) || O(n) space complexity 

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 0:
            return 0 
        
        left = []
        leftMax = height[0]
        for i in height: 
            leftMax = max(leftMax, i) 
            left.append(leftMax) 

        right = []
        rightMax = height[-1] 
        for j in height[::-1]:
            rightMax = max(rightMax, j) 
            right.append(rightMax) 
        right.reverse()
        minHeight = [] 
    
        for i in range(0, len(left)):
            minHeight.append( min(left[i], right[i])) 
        c = 0 
        water = 0 
        for k in height:
            if k < minHeight[c]: 
                water += minHeight[c] - k 
            else: 
                water += 0 
            c += 1 
        return water
        