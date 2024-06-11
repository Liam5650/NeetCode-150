class MinStack:

    def __init__(self):

        # Initialize a stack to hold values in order, and another for the minimum values encountered in order
        # This works since lists function as stacks in python
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # We have to also add the val to the minStack if it is the smallest encountered
        if self.minStack != [] and self.minStack[-1] >= val: self.minStack.append(val)
        elif self.minStack == []: self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()

        # If the value was the smallest, also pop it off the minStack
        if val == self.minStack[-1]: self.minStack.pop()

    # The values can now simply be determined by checking the top of the stack
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]