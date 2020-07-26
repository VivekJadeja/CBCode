#Next greater element using a stack
# O(n) TC

def next_greater_element(lst):
    s = MyStack()
    res = [-1] * len(lst)
    # Reverse iterate list
    for i in range(len(lst) - 1, -1, -1):
        # if stack has elements:
        if not s.is_empty():
            # While stack has elements
            # and current element is greater than top element
            # pop all elements
            while not s.is_empty() and s.top() <= lst[i]:
                s.pop()
        # if stack has an element
        # Top element will be greater than ith element
        if not s.is_empty():
            res[i] = s.top()
        # push in the current element in stack
        s.push(lst[i])

    for i in range(len(lst)):
        print(str(lst[i]) + " -- " + str(res[i]))
    return res


nge = next_greater_element([4, 6, 3, 2, 8, 1, 9, 9, 9])