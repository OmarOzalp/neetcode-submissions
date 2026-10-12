from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return the k most frequent elements in the list. 

        most_common = Counter(nums).most_common(k)
        output = []
        for m in most_common:
            output.append(m[0])

        return output
        