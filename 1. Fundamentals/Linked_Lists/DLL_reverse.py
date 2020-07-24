# Reverse a double linked list

def DLL_reverse(self):
    curr = self.head
    prv = None
    while curr:
        nxt = curr.next
        curr.next = prv
        curr.prev = nxt
        prv = curr
        curr = curr.next
    self.head = prv

# Checking if a linked list has a cycle with two pointers fast and slow
# fast will move 2 positions at a time and slow will move one
# if fast catches up to slow, then there is a cycle
# if fast or fast.next becomes null at any point, then there is no cycle
def has_cycle(self):
    fast = self.head
    slow = self.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

# Checking for the value at the middle node of a linked list
# O(n) time complexity since we are using two pointers just like has_cycle
def find_mid(self):
    if self.isEmpty():
        return -1
    curr = self.head
    if curr.next == None: # Since there is only one element in the list, we will return its value
        return curr.data
    
    # to check the rest of the list we will use 2 pointers. Just like the has_cycle pointers.
    mid_node = curr
    curr = curr.next.next

    while curr:
        mid_node = mid_not.next
        curr = curr.next
        if curr:
            curr = curr.next
    if mid_node:
        return mid_node.data
    return -1
