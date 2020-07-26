# Reverse the first k elements of a queue

# we will implement this by dequeueing the first k elements
# and pushing them into a stack
# stack.push(queue.dequeue())
# then we will pop the elements from stack and enqueue to queue
# then we will dequeue the rest of the elements range(size - k)
# and enqueue them right away queue.enqueue(queue.dequeue())

from collections import deque

def reverseK(queue, k):
    if len(queue) == 0 or k > len(queue) or k < 0:
        return None
    
    stack = deque()
    for i in range(k):
        stack.append(queue.popleft())
    
    for i in range(len(stack)):
        queue.append(stack.pop())
    
    size = len(queue)

    for i in range(size - k):
        queue.append(queue.popleft())
    
    return queue

if __name__ == "__main__":
    q = deque()
    for i in range(1,11):
        q.append(i)
    print(reverseK(q, 10))
    
    