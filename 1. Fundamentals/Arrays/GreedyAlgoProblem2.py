# Remove K digits
# given a non negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible

# We will go through the string and delete the number that is greater than the previous number

class Solution:
    def removeKdigits(self, num, k):
        stack = []
        for num in num:
            while (stack and k and int(stack[-1]) > int(num)):
                stack.pop()
                k -= 1
            stack.append(num)
        if k:
            stack = stack[:-k]
        cur = 0
        while (cur < len(stack) and stack[cur] == '0'):
            cur += 1
        stack = stack[cur:]
        if not stack:
            return "0"
        return "".join(stack)

num = "1432219"
k = 3
