class MinStack:

    stack = None
    minSequence = None

    def __init__(self):
        self.stack = deque([])
        self.minSequence = deque([])

    def push(self, val: int) -> None:
        if self.stack is not None and self.minSequence is not None:
            self.stack.append(val)
            if len(self.minSequence) > 0:
                self.minSequence.append(min(val, self.minSequence[-1]))
            else:
                self.minSequence.append(val)

    def pop(self) -> None:
        if self.stack is not None and self.minSequence is not None:
            self.stack.pop()
            self.minSequence.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else 0

    def getMin(self) -> int:
        return self.minSequence[-1] if self.minSequence else 0