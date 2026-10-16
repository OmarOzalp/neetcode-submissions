from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        chars = {}
        for c in s1: 
            chars[c] = chars.get(c, 0) + 1

        if len(s2) < len(s1):
            return False
        
        l = 0 
        r = 0
        window = {}
        while r < len(s2):
            if r < len(s1):
                window[s2[r]] = window.get(s2[r], 0) + 1
            else:
                window[s2[r]] = window.get(s2[r], 0) + 1
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    window.pop(s2[l])
                l+=1 
            r+=1

            if window == chars:
                return True
        return False



                


        


        
        