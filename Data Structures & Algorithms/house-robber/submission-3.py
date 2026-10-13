class Solution:
    def rob(self, nums: List[int]) -> int:

        # given an integer array of houses. 
        # cannot rob two adjacent houses. 
        # The best we can do is either we rob 
        # this house or the house before it. 

        r1, r2 = 0, 0 

        for num in nums:
            t = max(num + r1, r2)
            r1 = r2
            r2 = t
        return r2
            

        