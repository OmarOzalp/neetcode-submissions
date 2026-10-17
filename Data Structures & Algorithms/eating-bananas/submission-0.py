class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # integer piles, number of banas in ith pile. 
        # num hours needed to eat all bananas.
        # need to decide a number of hours per eating rate K. 
        lo = 1
        hi = max(piles)

        def can_finish(k):
            hours = 0
            for p in piles:
                hours += (p + k - 1) // k   # ceil(p / k) without floats
            return hours <= h
        
        while lo < hi:
            mid = (lo + hi)//2
            if can_finish(mid):
                hi = mid
            else:
                lo = mid+1
        
        return hi
            
        