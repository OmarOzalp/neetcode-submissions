class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # return the indices such that nums[i] + nums[j] == target
        # Alright say we have an integer: n. Our target is now
        # target - n: Right. 
        # What we can do is create a HashSet

        s = {}
        for i, n in enumerate(nums):
            if target - n in s:
                return [s[target - n],i]
            s[n] = i
            

            

        