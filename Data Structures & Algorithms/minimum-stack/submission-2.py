class MinStack:

    def __init__(self):
        self.stack = []   
        self.minstack = []     
        self.small = float("inf")
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.small:
            self.small = val
            self.minstack.append(val)

    def pop(self) -> None:
        a = self.stack.pop()
        if self.minstack and self.minstack[-1] == a:
            self.minstack.pop()
            if self.minstack:
                self.small = self.minstack[-1]
            else:
                self.small = float("inf")

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
