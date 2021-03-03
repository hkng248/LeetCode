
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