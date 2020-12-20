class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return self.plusOneHelper(digits, len(digits) - 1) 
    
    def plusOneHelper(self, digits, index):
        if index < 0:
            digits.insert(0,1) 
            return digits 
                
        if(digits[index] + 1 == 10): 
            digits[index] = 0 
            return self.plusOneHelper(digits, index - 1) 
        else:
            digits[index] += 1 
        return digits 