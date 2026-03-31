class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.stack:
            min_val = self.stack[0]
            for i in range(1,len(self.stack)):
                if min_val > self.stack[i]:
                    min_val = self.stack[i]
            return min_val

        else:
            return null
        
