# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n+m) runtime. n is size of listA, m is size of listB. O(1) SC
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a = 0
        len_b = 0
        a = headA
        b = headB
        
        while headA:
            len_a += 1
            headA = headA.next
            
        while headB:
            len_b += 1
            headB = headB.next
        
        if (len_a > len_b):
            diff = len_a - len_b
            while diff:
                a = a.next
                diff -=1
        
        elif( len_b > len_a ):
            diff = len_b - len_a
            while(diff):
                b = b.next
                diff -= 1
        
        while a and b:
            if a == b:
                return a
            a = a.next
            b = b.next
        return None
            