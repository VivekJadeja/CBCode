# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(1) TC and SC
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and fast.next: # While they are not None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
            