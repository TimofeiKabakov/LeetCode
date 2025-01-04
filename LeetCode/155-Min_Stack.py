class MinStack:

    def __init__(self):
        self.minVals = []
        self.stack = []

    def push(self, val: int) -> None:
        if not len(self.minVals) or val < self.minVals[-1]:
            self.minVals.append(val)
        elif val >= self.minVals[-1]:
            self.minVals.append(self.minVals[-1])

        self.stack.append(val)

    def pop(self) -> None:
        self.minVals.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]
        