class Solution:
    def reverseBits(self, n: int) -> int:
        # We want to reverse the bits. 
        # So that everything is flipped. 
        # lets try with 0011 we want 1100 
        res = 0 
        for i in range(32):
            res <<= 1
            res |= n&1
            n >>= 1
         
        return res



        