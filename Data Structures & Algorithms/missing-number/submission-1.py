class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # we want the single number that is missing. 
        #0,1,2,3, 
        
        n = len(nums)
        s = (n*(n+1))//2
        

        return s - sum(nums)
        