# To solve the problem of checking whether the parentheses are valid,
# we have to use a stack

# We will store all of the left facing parentheses
# pop every time we see right parentheses
# there can never be more right parentheses
# so if you pop when the stack is empty, it means
# you have more right parentheses than left.Thus, invalid
# Also, if stack is not empty at the end, it is invalid
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    def peek(self):
        return self.head
    
    def size(self):
        return self._size
    
    def __str__(self):
        curr = self.head
        out = ""
        while curr:
            out += str(curr) + " "
            curr = curr.next
        return out
    
    def isEmpty(self):
        return self._size == 0
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        if self.isEmpty():
            return
        curr = self.head
        self.head = self.head.next
        self._size -= 1
        return curr

def is_val_Paren(parenstr):
    stack = []
    parens = ["(", ")", "[", "]", "{", "}"]
    for char in parenstr:
        idx = parens.index(char)
        if idx % 2 == 0: #if it is the same index as the open parentheses
            stack.append(char)
        else: #if it is a closed parentheses
            if len(stack) == 0: # if stack is empty
                return False
            else: # if stack is not empty
                prev_char = stack.pop() # check the type of open parenthesis being popped
                if prev_char != parens[idx - 1]: # compare it to the open parentheses before the specific closing parenthesis to make sure they match
                    return False

    return len(stack) == 0

if __name__ == "__main__":
    val_paren_str = "[(())]"
    inval_paren_str1 = "([(())))"
    inval_paren_str2 = "(())}())"

    print(is_val_Paren(val_paren_str))
    print(is_val_Paren(inval_paren_str1))
    print(is_val_Paren(inval_paren_str2))
