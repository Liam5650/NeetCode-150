class Solution:
    def isValid(self, s: str) -> bool:

        # Use a list as a stack
        stack = []

        for bracket in s:

            # Push left brackets to the stack
            if bracket in ['(','{','[']:
                stack.append(bracket)
            
            else:

                # Pop the left bracket if one exists, and check to see if it matches the right bracket
                if stack != []: 
                    top = stack.pop()
                    if not (top == '(' and bracket == ')' or
                            top == '{' and bracket == '}' or
                            top == '[' and bracket == ']'):
                        return False
                
                # If the stack is empty and we encounter a right bracket, it isn't valid
                else:
                    return False

        # For the parentheses to be valid, the stack must be empty
        return stack == []