class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indices = [i for i, x in enumerate(s) if x == c] 
        if indices: 
            prev = indices.pop(0); next = prev 
            if indices: 
                next = indices.pop(0)
    
        result = [] 
        for i in range(0, len(s)): 
            if s[i] == c: 
                prev = i 
                if i == next: 
                    prev = next 
                    if indices:
                        next = indices.pop(0)
            result.append(min( abs(prev - i), abs(next - i)))
        return result 