class Solution:
    def rob(self, nums: List[int]) -> int:
        # We cxan either choose the firs thouse. 
        # or the last house. never both, So we can do 2. 
        # starting with the first house, and starting with the last house, and then pick the best one.

        l = len(nums)
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums[1], nums[0])
        r1, r2 = 0, 0 
        r3, r4 = 0, 0

        for i in range(len(nums)):
            if i < len(nums)-1:
                t = max(nums[i]+r1, r2)
                r1 = r2
                r2 = t
            if i >= 1:
                t = max(nums[i]+r3, r4)
                r3 = r4
                r4 = t
        

        
        return max(r2, r4)
        

        