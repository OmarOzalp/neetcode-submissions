
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # what we can do is remove our right to the right. 
        #
        
        chars = {}
        for c in t:
            chars[c] = chars.get(c, 0) + 1
        
        output = ""
        if len(s) < len(t):
            return output
        
        l = 0 
        r = 0 
        chars_missing = len(t)

        while r < len(s):
            if s[r] in chars:
                if chars[s[r]] > 0:
                    chars_missing -= 1
                chars[s[r]] -= 1
            while chars_missing == 0:
                if r - l + 1 < len(output) or output == "":
                    output = s[l:r+1]
                if s[l] in chars:
                    chars[s[l]] += 1
                    if chars[s[l]] > 0:
                        chars_missing += 1
                l += 1 
            r+=1
        
        return output
            

    
