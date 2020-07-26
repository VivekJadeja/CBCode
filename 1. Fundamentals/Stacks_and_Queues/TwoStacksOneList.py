#Implement two stacks using one list (array)

class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.top1 = -1
        self.top2 = self.size
    
    def push1(self, value):
        # if there is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = value
        else:
            print("Stack Overflow")
            exit(1)
    
    def push2(self, value):
        if self.top1 < self.top2 -1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = value
        else:
            print("Stack Overflow")
            exit(1)
    
    def pop1(self):
        if self.top1 >= 0: # If there is an element in stack1
            value = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return value
        else:
            print("Stack Underflow")
            exit(1)

    def pop2(self):
        if self.top2 < self.size: # If there is an element in stack2
            value = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return value
        else:
            print("Stack Underflow")
            exit(1)

stack = TwoStacks(10)
stack.push1(20)
stack.push2(20)

print(stack.pop1())
stack.push1(100)

