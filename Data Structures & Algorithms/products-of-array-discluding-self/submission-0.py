class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # We want a product of everything else except self. 
        # output[i] product of everything else except nums[i]
        # 1. What we can do is product everything together
        # 2. then go through and divide each output by output i.
        # We want to do it without using the div operator
        # [1,2,4] so we have [8, 4, 2]
        # Can we build based on eariler. 
        # 
        pref = [1] * len(nums)
        suf = [1] * len(nums)

        for i in range(1, len(nums)):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(len(nums) - 2, -1, -1 ):
            suf[i] = nums[i + 1] * suf[i + 1]
        
        return [suf[i] * pref[i] for i in range(len(nums))]
        
        