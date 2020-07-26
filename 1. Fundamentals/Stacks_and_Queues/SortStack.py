# Here we will learn how to recursively sort a stack
# without using any other data structure
class Stack:
    def __init__(self):
        self.stack_list = []

    # All of these are O(1) time complexity and space complexity
    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()

# O(n^2) TC
def sort_stack(stack):
    if not stack.is_empty():
        value = stack.pop()

        sort_stack(stack)

        insert(stack, value)

def insert(stack, value):
    if stack.is_empty() or value < stack.peek():
        stack.push(value)
    else:
        temp = stack.pop()
        insert(stack, value)
        stack.push(temp)

stack = Stack()
for i in range(0,9,2):
    stack.push(i)
    print(stack.peek())
    stack.push(i-1)
    print(stack.peek())

sort_stack(stack)

print([stack.pop() for i in range(stack.size())])