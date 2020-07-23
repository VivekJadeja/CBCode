# A dictionary is a hash map
# Use key value pairs where the key is hashed from a hash function
# all key, value pairs are stores in an array
# The hash function is used to find the index in the array where the key, value paired is stored
# because we get the index from the function after putting in the key

# A hash function is just a function that takes in a key and returns an integer value between the range [0,1,2,...,M-1]
# M is a large prime number that is used as the modulus divisor, which means it is the size of our hash table
# The large M we choose, the more key-value pairs the hash map can store because there are more available spots
# [0,1,2,...,M-1]
def hash_integer(integer_key):
    M = 97
    return integer_key % 97

# To has strings we have to find the number of characters in the alphabet it is using.
# For example, if it is the ASCII characters, there are 256 characters in the alphabet.
def hash_string(string_key):
    M = 1001
    # R is the number of letters of the alphabet. ASCII has R = 256
    R = 256
    hash_value = 0
    for char in string_key: # In order to get the has value, we must use the formula on each character
        hash_value = (hash_value * R + int(char)) % M
    return hash_value

# All hash functions should be:
#   Deterministic - The same key will always produce the same hash value
#   Efficient - Should be fast to compute
#   Uniform - Should distribute the keys uniformly


# Here are examples of bad hash functions that break these rules:

def non_deterministic_hash(integer_key): # This function is bad because it can produce the same hash for multiple keys
    M = 97
    current_time_int = int(time.time())
    return current_time_int % 97

def non_efficient_hash(integer_key): # This function is bad because it is squaring the integer key using 2 for loops. O(n^2) runtime
    M = 97
    hash_value = 0
    for i in range(integer_key):
        for j in range(integer_key):
            hash_value += 1
    return hash_value % M

def non_uniform_hash(integer_key): # This function is bad because it maps every key to index 1
    return 1


#-------------------------------------------------------------------------------------------------
# put(key, value) is done in O(1) runtime
# get(key) is also  done in O(1) runtime

# SEPARATE CHAINING HASH MAP
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
class Separate_Chaining_Map:
    # O(n) time and space complexity because it's making a new node object for each index in the size of the array
    def __init__(self, capacity):
        self.map = [Node(None, None) for _ in range(capacity)]
    
    # O(1) time and space b/c just performing a simple operation
    def hashedIndex(self, key):
        return key % len(self.map)

    # O(n) worst case is if there are many collisions and it will have to go through the entire linked list at an index
    # O(1) space complexity because we are not creating additional space. We are using a map that's already created
    def put(self, key, value):
        idx = self.hashedIndex(key)
        cur = self.map[idx] # We need to have a pointer to the first node in the linked list
        while cur.next: # As long as there is a node next to the one we are at
            if cur.next.key == key: # if the node has the key
                cur.next.value = value # replace its value with the new value and then exit
                return
            cur = cur.next # Move to the next node until we are either at the last node or the keys match
        cur.next = Node(key, value) # The next node will be the new node if there isn't one there

    # O(n) worst case runtime if we have to go through the linked list
    # O(1) space complexity
    def get(self, key):
        idx = self.hashedIndex(key)
        cur = self.map[idx]
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next

    # O(n) worst case runtime if we have to traverse
    # O(1) space complexity
    def delete(self, key):
        idx = self.hashedIndex(key)
        prv = self.map[idx]
        cur = prv.next
        while cur:
            if cur.key == key:
                prv.next = cur.next
            prv = cur
            cur = cur.next

    # O(n) regardless of size because we are going to print everything so we have to traverse through it all
    # O(n) space complexity because we are making a string adding each element
    def __str__(self):
        out = ""
        for idx in range(len(self.map)):
            cur = self.map[idx].next
            out += str(cur.key) + "|"
            while cur:
                out += str(cur.value) + " "
                cur = cur.next
            out += "\n"
        return out

if __name__ == "__main__":
    hash_map = Separate_Chaining_Map(3)
    for i in range(10):
        hash_map.put(i, i * 2)
    
    print(hash_map)
    print(hash_map.get(4))
    for i in range(3):
        hash_map.delete(i)
    print(hash_map)


