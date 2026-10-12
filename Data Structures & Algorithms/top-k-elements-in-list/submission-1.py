import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return the k most frequent elements in the list. 
        c = Counter(nums)
        # we need to keep a increasing heap
        h = []
        #h = [3, 4, 5]

        for n, count in c.items():
            if len(h) < k:
                heapq.heappush(h, (count, n))
            else:
               heapq.heappushpop(h, (count,n))

        return [n for _, n in h]



        