from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we want to group all anagrams together into sublists
        
        d = {}
        seen = set()
        output = []
        for s in strs:
            sort = "".join(sorted(s))
            if sort in seen:
                d[sort].append(s)
            else:
                d[sort] = [s]
                seen.add(sort)

        return list(d.values())

        