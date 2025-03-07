class MyQueue:
    def __init__(self):
        self.write = []
        self.read = []

    def push(self, x: int) -> None:
        self.write.append(x)

    def pop(self) -> int:
        if not self.read:
            while self.write:
                self.read.append(self.write.pop())
        return self.read.pop()

    def peek(self) -> int:
        if not self.read:
            while self.write:
                self.read.append(self.write.pop())
        return self.read[-1]

    def empty(self) -> bool:
        return not self.read and not self.write
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()