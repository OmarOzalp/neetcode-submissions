class Solution:
    def climbStairs(self, n: int) -> int:

    # the number of ways to reach any step 
    # is the number of ways to reach the step before that + the number
    # of ways to reach the step before that. 

        dp = [1] * n
        if n >= 2:
            dp[0] = 1
            dp[1] = 2
        
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]