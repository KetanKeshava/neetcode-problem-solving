class MinStack:

    def __init__(self):
        self.stack = list()
        self.minStack = list()
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            if val < self.getMin():
                currentMin = val
            else:
                currentMin = self.getMin()
            self.minStack.append(currentMin)
    
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        
