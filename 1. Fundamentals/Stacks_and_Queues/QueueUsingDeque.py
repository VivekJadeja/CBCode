# This is basically a tutorial on creating a linear queue using the Deque operations from collections
# It is built in as a doubly linked list
# This deque can also be used as a linear queue
# all operations are O(1) time and space complexity since the two pointers are able to manage the front and end append/remove operations
import collections.deque

# Create the binary equivalent of a given integer
def find_bin(n):
    result = []
    myQueue = deque()
    myQueue.enqueue(1) # Starting with enqueueing 1 because if we want to print binary of 1, we just run the for loop once and dequeue into append result
    for i in range(n): # This works for edge case n = 0 because the for loop won't run and nothing gets appended to result
        result.append(str(myQueue.dequeue())) # append the value that is dequeued for each iteration, given sequence from 1 to n
        s1 = result[i] + "0" # Will add a 0 to result[i] which is the number that just got dequeued, meaning it will be the next number
        s2 = result[i] + "1" # Adding a 1 to the number that just got dequeued will give us the next next number
        myQueue.enqueue(s1)
        myQueue.enqueue(s2)
    return result

if __name__ == "__main__":
    print(find_bin(1))