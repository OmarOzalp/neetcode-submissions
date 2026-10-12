class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We can make a set with all the last seen 
        # charachters, and their location
        #zxyzxyz

        chars = {}
        left = 0 
        len_substring = 0 

        for right in range(len(s)):
            if s[right] in chars:
                left = max(left, chars[s[right]] + 1)
            chars[s[right]] = right

            len_substring = max(right - left + 1, len_substring)
        
        return len_substring

            
        