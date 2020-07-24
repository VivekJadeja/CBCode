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