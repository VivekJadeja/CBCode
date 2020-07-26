# We want to remove the Kth node from the end of a linked list

class Solution:
    # O(n) TC and O(1) SC
    def removeNthFromEnd(self, head, n):
        # Starting both pointers at the head
        p1 = head
        p2 = head
        for _ in range(n): # Iterate through and get the first pointer to the nth away from the beginning node
            p1 = p1.next
        if not p1: # If it does not exist, then it has moved n number of times and the head should be removed
            head = head.next
            return head
        while p1.next: # While p is not at the end, we will move the pointers
            p1 = p1.next # p2 will finally land on the node before the node we want to remove. Then we will point the current p2 to 2 nodes over
            p2 = p2.next
        p2.next = p2.next.next
        return head