class Stack:
    def __init__(self, elements: list = None):
        self.arr = [] if not elements else elements

    def push(self, element):
        self.arr.append(element)

    def push_many(self, *elements):
        print(type(elements))
        self.arr.extend(elements)

    def pop(self):
        return self.arr.pop() if len(self.arr) > 0 else None

    def peek(self):
        return self.arr[-1] if len(self.arr) > 0 else None

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.arr)


if __name__ == "__main__":

    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push_many(40, 50)

    while not stack.is_empty():
        print(stack.pop())
