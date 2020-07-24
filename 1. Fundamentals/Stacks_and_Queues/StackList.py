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


stack = Stack()
for i in range(5):  # Pushing values in
    stack.push(i)

print("peek(): " + str(stack.peek()))

for x in range(5):  # Removing values
    print(stack.pop())

print("is_empty(): " + str(stack.is_empty()))  # Checking if its empty