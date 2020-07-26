# We will make a queue from 2 stacks

# Creating our Stack class
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return self.size() == 0
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

# Now we will write the class for making the queue
# it will use 2 stacks

class newQueue:
    def __init__(self):
        self.main_stack = Stack()
        self.temp_stack = Stack()
    
    def enqueue(self, value):
        self.main_stack.push(value)
        print(str(value) + " enqueued")
       
    
    def dequeue(self):
        if self.temp_stack.isEmpty():
            if self.main_stack.isEmpty():
                return None # if both stacks are empty, return None
            # If temp stack is empty, but not main
            # Transfer all elements to temp stack
            while not self.main_stack.isEmpty():
                value = self.main_stack.pop()
                self.temp_stack.push(value)
                # basically, you are reversing the stack
                # by popping from main and putting it on temp
                # if you pop from temp, you get the original order
                # of pushing into the first stack
                # which is basically a queue
        temp = self.temp_stack.pop() # this is the oldest element in the queue, the first one pushed
        print(str(temp) + " dequeued")
        return temp
    
if __name__ == "__main__":
    queue = newQueue()
    for i in range(4):
        queue.enqueue(i)

    for i in range(100):
        queue.dequeue()