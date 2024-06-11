class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        # Use a stack, and push any int value
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            
            # If it is an operand, pop the top values on the stack and push the result
            else:
                val1 = stack.pop()
                val2 = stack.pop()

                if token == "+": stack.append(val2 + val1)
                elif token == "-": stack.append(val2 - val1)
                elif token == "*": stack.append(val2 * val1)
                elif token == "/": stack.append(int(val2 / val1))
        
        # The answer is the only thing remaining in the stack
        return stack.pop()