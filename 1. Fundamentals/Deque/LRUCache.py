# To sole LRU Cache we must use a double linked list and a hash map

# The doubly linked list will store the key-value pairs
# We will need to add key as a field to our node class sine we are keeping track of the key-value pairs
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
# Within our double linked list, we will keep the most recently used items at the front of the linked list (head)
# and the LRU items at the back of the linked list (tail)
# Then we will use a hash map to input keys to the double linked list node containing the key-value pair
class DoublyLinkedList():
    def __init__(self):
        # Dummy nodes to keep track of front and back
        # We will also have them point to each other to start off the doubly linked list
        self.head = Node("head", "head")
        self.tail = Node("tail", "tail")
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


    def addToFront(self, key, value):
        curr_node = Node(key, value)
        nxt = self.head.next
        nxt.prev = curr_node
        curr_node.next = nxt
        self.head.next = curr_node
        curr_node.prev = self.head

    # returns a key so that the hash map can use the key to delete the associated key-value pair
    def removeBack(self):
        node_to_delete = self.tail.prev
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        return node_to_delete.key


class LRU_Cache:
    def __init__(self, capacity):
        # initializing the double linked list
        self.nodes = DoublyLinkedList()
        # capacity of the hash map
        self.capacity = capacity
        # current size of hash map
        self.size = 0
        # Hash map of items in the cash
        self.inCache = {}
        # way to made nodes

    # If key exists in the hash map, we will move the node for it to the front of the LL
    #   else it will return None if it is not in the hash map
    def get(self, key):
        if key in self.inCache:
            value = self.inCache[key]
            self.nodes.delete(key)
            self.nodes.addToFront(key, value)
            return value
        return 

    # If key already exists in the cache, we will replace it in the cache and update value of old node in LL and move to front
    # If adding this will exceed the capacity,  then we will delete the LRU node from the back
    # In all cases, we will just add this to the front
    def set(self, key, value):
        if key in self.inCache:
            self.nodes.delete(self.inCache[key])
            self.inCache[key] = value
            self.nodes.addToFront(key, value)
        else:
            self.inCache[key] = value
            self.size += 1
            self.nodes.addToFront(key, value)
            if self.size > self.capacity:
                temp = self.nodes.removeBack()
                del inCache[temp]
                self.size -= 1

# THIS FUNCTION IS ONLY FOR CHECKING OUTPUTS
    def __str__(self):
        curr = self.nodes.head.next
        out = ""
        mapout = ""
        while curr:
            if curr is not self.nodes.tail:
                out += str(curr.key) + " " + str(curr.value) + " "
            curr = curr.next
        return out


if __name__ == "__main__":
    lru = LRU_Cache(3)
    lru.set(1,1)
    lru.set(2,2)
    lru.set(3,3)
    print(lru)
    print(lru.inCache)

    print(lru.get(2))