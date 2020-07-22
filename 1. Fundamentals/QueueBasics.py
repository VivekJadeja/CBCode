# Queues also use linked lists similarly to stacks
# We will enqueue and dequeue stuff kind of like inserting and removing from a stack/LL

# CREATING A QUEUE

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    # O(1) TC and SC
    def __init__(self):
        self.head = None
        self.tail = self.head
        self._size = 0 # underscore used because you can't name it the same as the function at the bottom
    
    # O(1) Time and Space complexity. We are not traversing the list for the queue, we are only setting certain variables = to something
    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty(): # If it is empty and you add a node, then the head and tail both point to the new node
            self.head = new_node
            self.tail = new_node
        else: # If it is not empty and you add a node, then the tail.next becomes new node and then you set self.tail = new node
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    # O(1) time and space complexity since we are just changing the values of some variables a fixed number of times. We are not using any additional space
    def dequeue(self):
        if self.isEmpty(): # Cannot dequeue if it is empty so you return None
            return
        else: # If the queue is not empty, then you would hold the head node in a temporary variable and then you would set self.head = self.head.next
            # and return the temporary variable holding what we just removed from the queue
            curr_node = self.head
            self.head = self.head.next
            if self._size == 1: # Edge case if there is one node, we need to make sure the tail is None now that we removed the one node
                self.tail = None
            self._size -= 1
            return curr_node.data

    # These 3 are all O(1) TC and SC
    def size(self):
        return self._size

    def isEmpty(self):
        return self._size == 0
    
    def peek(self):
        print(self.head.data)
    
    # O(n) time complexity and O(n) space complexity
    def items(self):
        curr = self.head
        out = ""
        while curr:
            out += str(curr.data) + " "
            curr = curr.next
        return out
        
if __name__ == "__main__":
    queue = Queue()
    print(queue.isEmpty())
    for i in range(3):
        queue.enqueue(i)
    print(queue.items())
    for _ in range(4):
        print(queue.dequeue())
    
    print("Printing queue items", queue.items(), "Done")

    for i in range(2,4):
        queue.enqueue(i)
    print(queue.items())