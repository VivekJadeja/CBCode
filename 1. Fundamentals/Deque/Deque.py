# A Deque is a double ended Queue
# Supports all add/remove from front and end in O(1) time since it uses 2 pointers, one for head, one for tail.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Deque:
    #O(1) constant time and space
    def __init__(self):
        self.head = Node("head")
        self.tail = Node("tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        self._size = 0

    #O(1) constant time and space
    def isEmpty(self):
        return self.getSize() == 0

    #O(1) constant time and space
    def getSize(self):
        return self._size

    #O(1) constant time and space
    def insertFront(self, value):
        new_node = Node(value)
        first_node = self.head.next
        self.head.next = new_node
        first_node.prev = new_node
        new_node.prev = self.head
        new_node.next = first_node
        self._size += 1

    #O(1) constant time and space
    # No need to traverse the Deque because we already have a pointer pointing to tail!
    def insertLast(self, value):
        new_node = Node(value)
        prv = self.tail.prev
        prv.next = new_node
        self.tail.prev = new_node
        new_node.prev = prv
        new_node.next = self.tail
        self._size += 1

    #O(1) constant time and space
    def deleteFirst(self):
        if self.isEmpty():
            return
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self._size -= 1

    #O(1) constant time and space
    def deleteLast(self):
        if self.isEmpty():
            return
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self._size -= 1

    #O(n) linear time and space since we are iterating and also adding to a string
    def __str__(self):
        cur = self.head.next
        out =  ""
        while cur:
            if cur is not self.tail:
                out += str(cur.value) + " "
            cur = cur.next
        return out

if __name__ == "__main__":
    dq = Deque()
    for i in range(1,6):
        dq.insertFront(i)
    for i in range(6,11):
        dq.insertLast(i)
    print(dq)
    dq.deleteFirst()
    print(dq)
    dq.deleteLast()
    print(dq)