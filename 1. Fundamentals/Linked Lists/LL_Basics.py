# Basics of a Linked List

# Inserting into a Linked List
#   Step 1: Create New Node
#   Step 2: Have new_node.next = self.head
#   Step 3: set self.head = new_node

# Deleting from a LL
#   If you want to remove the head, then have the self.head = curr_node.next and set curr_node = None
#   If it is the tail and curr_node.next = None, prv = curr_node.prev, prv.next = None, curr_node.prev = None, curr_node = None
#   Otherwise if it is another node somewhere in the LL
#   Step 1: prv = curr_node.prev
#   Step 2: nxt = curr_node.next
#   Step 3: nxt.prev = prv
#   Step 4: prv.next = nxt
#   Step 5: curr_node = None

# Traversing a LL
#   curr_node = self.head
#   while curr_node is not None:
#       curr_node = curr_node.next

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    # Run time of printing out the entire LL is O(n)
    # O(n) space complexity because we are adding to a new string for size of n
    def __str__(self): # Prints contents of LL
        out = ""
        curr_node = self.head
        while curr_node: # loop takes O(n)
            out += str(curr_node.data) + "|" # Adding to str takes O(1) runtime but O(n) space complexity
            curr_node = curr_node.next
        return out

    # Run time of adding to front of LL is O(1)
    # Space complexity is O(1)
    def insertFront(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1

    # Time complexity/run time is O(n)
    # Space complexity is O(1)
    def insertLast(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
        self._size += 1

    # O(1) time and space complexity to remove from beginning of a LL
    def removeBeginning(self):
        assert(self.size() > 0) # Can use this or you can just check if the self.head exists
        if self.head:
            curr_node = self.head
            nxt = curr_node.next
            self.head = nxt
            curr_node.next = None
            curr_node = None
        self._size -= 1
        
    # Returning size is O(1) for both because we are just return a value from a variable
    def size(self):
        return self._size

if __name__ == "__main__":
    linkedlist = LinkedList()
    for i in range(1,6):
        linkedlist.insertFront(i)
    #Should print 1|2|3|4|5
    print(linkedlist)
    linkedlist.removeBeginning()
    linkedlist.removeBeginning()
    print(linkedlist)
    for i in range(6,11):
        linkedlist.insertLast(i)
    print(linkedlist)