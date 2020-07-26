# Reverse Polish is basically postfix notation

class Solution:
    # O(n) TC and O(n) SC
    # This one is for integer only annd truncates division
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c not in '+-*/':
                stack.append(int(c))
            else:
                v2=stack.pop()
                v1=stack.pop()
                if c=='+':
                    stack.append(v1+v2)
                elif c=='-':
                    stack.append(v1-v2)
                elif c=='*':
                    stack.append(v1*v2)
                else:
                    stack.append(int(v1/v2))
        return stack[0]