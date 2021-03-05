
class FreqStack:
    mf = None 
    f = None 
    fs = None 
    
    def __init__(self):
        self.mf = 0 
        self.f = defaultdict(int) 
        self.fs = defaultdict(list) 

    def push(self, x: int) -> None:
        self.f[x] += 1 
        self.mf = max(self.mf, self.f[x]) 
        self.fs[self.f[x]].append(x)
        
    def pop(self) -> int:
        c = self.fs[self.mf][-1] 

        self.fs[self.mf].pop() 
        self.f[c] -= 1 

        if len(self.fs[self.mf]) <= 0: 
            del self.fs[self.mf] 
            self.mf -= 1 
        return c 

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()


### TLE (This solution does not work)

# class FreqStack:
#     e = None 
#     eFreq = None 
#     mF = None 
    
#     def __init__(self):
#         self.e = [] 
#         self.eFreq = {} 
#         self.mf = 0 
        
#     def push(self, x: int) -> None:
#         self.e.append(x)
#         if x in self.eFreq.keys():
#             self.eFreq[x] += 1 
#         else:
#             self.eFreq[x] = 1 
#         self.mf = max(self.eFreq[x], self.mf)
        
#     def find_last(self, lst, elm):
#         gen = (len(lst) - 1 - i for i, v in enumerate(reversed(lst)) if v == elm)
#         return next(gen, None)        
        
#     def pop(self) -> int:
#         #find value with most frequent occurrence 
#         x = [k for k,v in self.eFreq.items() if v == self.mf]
#         #find which value is closest to the top
#         maxI = 0
#         for i in x: 
#             maxI = max(maxI, self.find_last(self.e, i))
#         v = self.e[maxI]
#         self.eFreq[v] -= 1
#         del self.e[maxI] 
        
#         if len(x) == 1:
#             self.mf -= 1 
#         return v 