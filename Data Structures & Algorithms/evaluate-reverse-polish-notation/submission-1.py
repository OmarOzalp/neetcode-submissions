class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Okay, we have a stack, once we reach a value that is not num. then we can pop two from the stack. 

        ops = '+-*/'
        stack = []

        for token in tokens:
            if token in ops:
                print(f"1:{token}")
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                if token == "+":
                    pu = val1 + val2
                elif token == "-":
                    pu = val1 - val2
                elif token == "*":
                    pu = val1 * val2
                else:
                    pu = val1 / val2
            else:
                pu = token
            
            stack.append(int(pu))
        
        return stack[0]


        