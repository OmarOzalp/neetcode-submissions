class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # max_char_count + k = window_size
        # if max_char_count + k = window_size
        # we can increase window.
        # otherwise we decrease

        chars = {}
        max_char_count = 0 
        left = 0 
        for right in range(len(s)):
            chars[s[right]] = chars.get(s[right], 0)+1
            max_char_count = max(chars[s[right]], max_char_count)
            if max_char_count + k < (right - left) + 1:
                chars[s[left]] -= 1
                left += 1

        
        return right - left + 1
        