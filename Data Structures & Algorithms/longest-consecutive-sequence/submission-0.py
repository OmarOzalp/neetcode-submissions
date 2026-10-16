class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Longest 
        s = set(nums)
        max_l = 0
        for num in s:
            if num - 1 in s:
                continue
            l = 1
            while num + 1 in s:
                l+= 1
                num += 1
            max_l = max(l, max_l)

        return max_l
        