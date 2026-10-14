class Solution:
    def hammingWeight(self, n: int) -> int:
        # We want the number of 1 bits:
        res = 0 
        while n: 
            n = n & (n-1)
            res += 1

        
        return res

        