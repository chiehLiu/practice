class MinStack:

    def __init__(self):
        self.stack = []

    # Time: O(1)
    # Space: O(n)
    # we are using a tuple to store the value and the min value
    def push(self, val: int) -> None:
        if len(self.stack):
            self.stack.append((val, min(val, self.stack[-1][1])))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
