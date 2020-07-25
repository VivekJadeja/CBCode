# Circular Queues

# Similar to linear(regular) queues, except the front and rear part of the queue point to the same location initially.
# Both ends are connected to form a circle
#   This is useful in the simulation of objects and event handling (do something when a particular event occurs)

# Priority Queue

# All elements have a priority associated with them and are sorted such that 
# the most prioritized object appears at the front and the least prioritized appears at the back.
# Priority queues are widely used in operating systems to determine which programs should be given more priority.

# Double-Ended Queue
# We've dealt with these before in the Deque section

# Acts as a queue from both back and front. Provides enqueue and dequeue from both ends in O(1) TC and SC
# Can act as a linear queue if needed.
# Python has a built in Deque class that can be imported from collections. 