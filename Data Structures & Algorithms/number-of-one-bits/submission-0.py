class Solution:
    def hammingWeight(self, n: int) -> int:
        # We want the number of 1 bits:
        binary = bin(n)
        s = 0 
        for digit in binary[2:]:
            s+=int(digit)
        
        return s

        