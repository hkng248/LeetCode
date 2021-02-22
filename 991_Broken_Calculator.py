class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if(X == Y):
            return 0 
        elif(X > Y):
            return X-Y 
        elif( Y % 2 == 0):
            Y //= 2 
        else:
            Y += 1 
        return 1 + self.brokenCalc(X, Y)
        
        