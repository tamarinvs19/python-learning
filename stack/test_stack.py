def test_stack1(stack):
    r = []
    for i in range(10):
        stack.append(i)
    for _ in range(5):
        r.append(stack.pop())
    while stack != []:
        r.append(stack.pop())

def test_stack2(stack):
    r = []
    for i in range(10):
        stack.push(i)
    for _ in range(5):
        r.append(stack.pop())
    while not stack.is_empty():
        r.append(stack.pop())
