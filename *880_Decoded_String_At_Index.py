

# Time Limit Exceeded 
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        tape = "" 
        for i in S:
            if i in "123456789": 
                tape =  str(tape) * int(i)
            else:
                tape += i 
        return tape[K-1]
        