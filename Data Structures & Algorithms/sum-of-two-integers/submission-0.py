class Solution:
    def getSum(self, a: int, b: int) -> int:
        # given two integers I need the sum without

        # What we can do is break it down. 
        
        # given 1, and 3
        # 01 and 11. 
        # 1 xor 1 = 0 
        # if 1 xor 1 = 1 then we check carry
        ret = 0 
        carry = 0 
        for i in range(32):
            a_bit = a&1
            b_bit = b&1
            curr_bit = cur_bit = a_bit ^ b_bit ^ carry

            carry = (a_bit & b_bit) | (carry & (a_bit ^ b_bit))
            if curr_bit:
                ret |= (1 << i)
            
            a >>= 1
            b >>= 1
        
        mask = 0xFFFFFFFF  # (1 << 32) - 1
        if ret > 0x7FFFFFFF:
            ret = ~(ret ^ mask)

        return ret




       


        





        