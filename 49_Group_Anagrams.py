class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {} 
        for i in strs: 
            iSort = ''.join(sorted(i))
            if iSort in anagramMap.keys():
                anagramMap[iSort].append(i)
            else:
                anagramMap[iSort] = [i]
        return list(anagramMap.values())
        



'''
# Python 3.6.5 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapOfLetters = {}
        mapOfWords = [] 
        for word in strs: 
            sortedLetters = ''.join(sorted(word))
            if(sortedLetters in mapOfLetters.keys()):
                currentList = mapOfLetters.get(sortedLetters)
                currentList.append(word)
                mapOfLetters[sortedLetters] = currentList
            else:
                mapOfLetters[sortedLetters] = [word] 
        for k in mapOfLetters.values():
            mapOfWords.append(k)
        return mapOfWords 
 '''
            
        
