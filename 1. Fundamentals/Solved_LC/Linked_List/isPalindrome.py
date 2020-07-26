# Checkins if the liked list is a palindrome
# Using two pointers. Fast and slow
# Works for all cases
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        slow, fast = self.reverse(slow), head
        
        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        
        return True
    
    def reverse(self, node):
        prev, curr = None, node
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev