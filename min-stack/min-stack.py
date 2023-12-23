class MinStack:

    # for a stack we add items and remove items from the top of the stack.
    # items below the top of the stack are always present in the stack until they are removed
    # hence to persist the min value from all the items in the stack, we represent every entry in our stack as a tuple
    # the first entry in the tuple corresponds to the actual value. 
    # the second entry in the tuple corresponds to the min value which will be min (current value, min(current top ))
    
    def __init__(self):
        # initialize an empty stack
        # each entry in our stack will be a tuple
        # first entry in the tuple will correspond to the actual value
        # second entry in the tuple will correspond to the min value
        self.stack = []
        

    def push(self, val: int) -> None:
        
        # if there are no items currently on the stack
        # in this case add the passed val and also 
        if (len(self.stack) == 0):
            self.stack.append((val, val))
            return
        
        # values are already existing in the stack
        # let us find out the current min value
        # currentMin will be equal to the min value correspondong to the top of the stack or the current val
        currentMin = min(self.stack[-1][1], val)
        self.stack.append((val, currentMin))
        return

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
