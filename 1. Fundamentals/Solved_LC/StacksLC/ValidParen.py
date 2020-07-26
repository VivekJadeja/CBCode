class Solution:
    # O(n) TC and O(n) SC b/c stack is created
    def isValid(self, s: str) -> bool:
        stack = []
        paren = ['(', ')', '{', '}', '[', ']']
        for char in s:
            idx = paren.index(char)
            if idx % 2 == 0:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    opposite = stack.pop()
                    if opposite != paren[idx-1]:
                        return False
        return len(stack) == 0
                
            