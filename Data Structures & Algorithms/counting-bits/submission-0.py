class Solution:
    def countBits(self, n: int) -> List[int]:

        # alright, at any power of 2, 
        # 110 6 << 11 3, 5 101 << 10 its a right shift + 1
        # if odd its a right shift and you add one, if even its a right shift, and you add zero:

        
        num_bits = [0] * (n+1)

        for i in range(1, n+1):
            if i % 2 == 1:
                num_bits[i] = num_bits[i//2] + 1
            else:
                num_bits[i] = num_bits[i//2]
        
        return num_bits
        