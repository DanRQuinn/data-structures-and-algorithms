from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        while self.stack1.top:
            self.stack2.push(self.stack1.pop())
        result = self.stack2.pop()
        while self.stack2.top:
            self.stack1.push(self.stack2.pop())
        return result
