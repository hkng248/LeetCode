class Solution:
    def reverse(self, x: int) -> int:
        limit = 2 ** 31 
        neg_limit = -1 * b 
        
        answer = 0
        negativeFlag = False 
        if(x < 0):
            negativeFlag = True 
        x = abs(x)
        multiplier = int(len(str(x))) - 1
        while( x  > 0):
            digit = x % 10 
            answer +=  (digit) * math.pow(10, multiplier)
            multiplier -= 1 
            x //= 10 
        
        if(negativeFlag):
            answer *= -1 
        if answer > b or answer < neg_b:
            return 0 
        
        return floor(answer)
            
        