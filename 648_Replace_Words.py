class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        prefixHash = set(dictionary)
        s = sentence.split(); r=[]
        for j in s: 
            t = "" 
            for c in j:
                if t in prefixHash: 
                    r.append(t)
                    t = ""
                    break 
                else:
                    t += c 
            if len(t) > 0:
                r.append(t)
        return (" ").join(r)
    
                    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        rootset = set(dictionary) 
        def replace(word):
            for i in range(1, len(word)): 
                if word[:i] in rootset: 
                    return word[:i]
            return word 
        return " ".join(map(replace, sentence.split()))
