class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.minimum = sys.maxsize

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minimum:
            self.minimum= val
            self.minStack.append(val)

        

        

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.minimum:
            self.minStack.pop()
            if len(self.minStack) > 0:
                self.minimum = self.minStack[-1]
            else:
                self.minimum = sys.maxsize
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum

        
