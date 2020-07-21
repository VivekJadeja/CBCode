# Detecting a Cycle in a Linked List

# We are going to use two pointers to see if there is a cycle.
# Both of them will start at the head.
# One pointer, the fast pointer, will move ahead 2 positions on each iteration of the while loop
# The second pointer, the slow pointer, will move ahead 1 position.
# If at any point, fast == None, meaning that it reaches the end of the linked list, we know there is no cycle
# If at any point, fast == slow, then there must be a cycle and we will return True
# There may be duplicate number in the linked list, but it doesn't matter because we are not comparing
# the content of each node, but rather the location/address of each node.
# This is a common algorithm when the length of the LinkedList is unknown

# O(n) time complexity because iterates through the entire linked list
# O(1) time complexity because we are only storing fixed numbers in variables. These variables are not scalable with input size like
# if we were adding to a list or string or linked list
def has_cycle(self):
    fast = self.head
    slow = self.head
    while fast and fast.next: # Checking if both fast and fast.next are not None for Edge case that LL is empty or only has 1 node
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False