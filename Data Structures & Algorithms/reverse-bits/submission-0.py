class Solution:
    def reverseBits(self, n: int) -> int:
        # We want to reverse the bits. 
        # So that everything is flipped. 
        # lets try with 0011 we want 1100 
        binary = bin(n)
        binary = binary[2:]
        binary = binary[::-1]
        while len(binary) < 32:
            binary += '0'
        
        return int(binary, 2)
         



        