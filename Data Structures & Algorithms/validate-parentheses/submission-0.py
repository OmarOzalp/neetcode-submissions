class Solution:
    def isValid(self, s: str) -> bool:
        o = {"}":"{", ")":"(", "]":"["}
        stack = []

        for c in s:
            if c in o: 
                if stack:
                    if stack.pop() == o[c]:
                        continue
                return False
            else:
                stack.append(c)
        
        return False if stack else True

        