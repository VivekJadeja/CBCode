# Under the hood, stacks are implemented using linked lists
#   top of stack is self.head
#   When we remove an item from the stack we move self.head to self.head.next
#   The insert method is also the same as a regular linked list where we loop through the list until the end and set the pointer for that to new node

#   MAKING A STACK

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    # Constructor/Initializer to create an empty stack
    # O(1) TC and SC to initialize the stack
    def __init__(self):
        self.head = None
        self._size = 0
    
    # Push an item onto the stack
    # O(1) time and space complexity
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def isEmpty(self):
        return self._size == 0 # Returns True if size is 0, returns False otherwise

    # Pop an item from stack
    # O(1) time and space complexity
    def pop(self):
        if self.isEmpty(): # First check if stack is empty to see if there is even anything to pop
            return
        else:
            curr_node = self.head
            self.head = self.head.next
            self._size -=1
            return curr_node.data

    # These two are also O(1) TC and SC
    def size(self):
        return self._size

    def peek(self):
        print(self.head.data)

    # Method to print contents of stack
    # O(n) TC and O(n) SC because we are traversing through all elements. SC is O(n) because we are storing all those elements
    def __str__(self):
        curr_node = self.head
        out = ""
        while curr_node:
            out += str(curr_node.data) + " "
            curr_node = curr_node.next
        return out




if __name__ == "__main__":
    stack = Stack()
    for i in range(5):
        stack.push(i)
    print(stack)

    for i in range(6):
        print(stack.pop())
