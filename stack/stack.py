class Stack :
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

stack2 = Stack()
stack1 = []

from timeit import timeit
print(timeit('test_stack1(stack)', number=1000, setup="from test_stack import test_stack1", globals={'stack': stack1}))
print(timeit('test_stack2(stack)', number=1000, setup="from test_stack import test_stack2", globals={'stack': stack2}))


