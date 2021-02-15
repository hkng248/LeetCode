class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        numberMap = defaultdict(list)
        index = 0 
        for j in mat: 
            numberMap[j.count(1)].append(index)
            index += 1
            
        result = [] 
        for i in sorted(numberMap.keys()):
            while k > 0 and numberMap[i]:
                result.append(numberMap[i].pop(0))
                k -= 1 
        return result 





class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        numberMap = defaultdict(list)
        index = 0 
        for j in mat: 
            numberMap[j.count(1)].append(index)
            index += 1 
        result = [] 
        for i in sorted(numberMap.keys()):
            for j in numberMap[i]: 
                result.append(j)
                k -= 1 
                if k == 0:
                    return result 
            if k == 0:
                break
        return result 
        