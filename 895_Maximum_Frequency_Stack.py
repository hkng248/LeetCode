### TLE (This solution does not work)

class FreqStack:
    e = None 
    eFreq = None 
    mF = None 
    
    def __init__(self):
        self.e = [] 
        self.eFreq = {} 
        self.mf = 0 
        
    def push(self, x: int) -> None:
        self.e.append(x)
        if x in self.eFreq.keys():
            self.eFreq[x] += 1 
        else:
            self.eFreq[x] = 1 
        self.mf = max(self.eFreq[x], self.mf)
        
    def find_last(self, lst, elm):
        gen = (len(lst) - 1 - i for i, v in enumerate(reversed(lst)) if v == elm)
        return next(gen, None)        
        
    def pop(self) -> int:
        #find value with most frequent occurrence 
        x = [k for k,v in self.eFreq.items() if v == self.mf]
        #find which value is closest to the top
        maxI = 0
        for i in x: 
            maxI = max(maxI, self.find_last(self.e, i))
        v = self.e[maxI]
        self.eFreq[v] -= 1
        del self.e[maxI] 
        
        if len(x) == 1:
            self.mf -= 1 
        return v 
            
            
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()