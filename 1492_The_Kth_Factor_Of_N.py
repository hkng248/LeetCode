class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1]
        i = 2
        while i <= n :
            if n % i == 0:
                factors.append(i)
            i += 1 
        if k <= len(factors):
            return factors[k - 1]
        return -1
        