import heapq
heap = []
# This heapq.heappush(item) ensures that heap[0] is the SMALLEST element.
# heappush() takes O(log n) time.
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)

# heappop() takes O(log n) time.
min_element = heapq.heappop(heap)
print(min_element) # 1
min_element = heapq.heappop(heap)
print(min_element) # 3
min_element = heapq.heappop(heap)
print(min_element) # 5

# If you have tuples, it will sort by the first element and use second element for ties.
heap = []
heapq.heappush(heap, (5, 'write code'))
heapq.heappush(heap, (7, 'release product'))
heapq.heappush(heap, (1, 'write spec'))
heapq.heappush(heap, (3, 'create tests'))
heapq.heappop(heap) # (1, 'write spec')

# Alternatively, say you have a class and you want to add them to a heapq. You will need to implement a '__lt__' (less than) comparator method.

class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Compare by name first, then by age if there's a tie.
    def __lt__(self, other):
        if self.name == other.name:
            return self.age < other.age
        return self.name < other.name

heap = []
heapq.heappush(heap, Person("Ann", '16'))
heapq.heappush(heap, Person("Bob", 14))
heapq.heappush(heap, Person("Sam", 12))
heapq.heappop(heap) # ("Ann", 16)

# Here's how to setup a heap of fixed size. Here's an example.
max_size = 20
heap = []
for i in range(0, 100):
    if len(heap) >= 20:
        # This will push i and then pop the smallest element.
        heapq.heappushpop(heap,i)
    else:
        heapq.heappush(heap, i)
print(len(heap)) # 20


# If you want to use a max heap, try the following. You can either change the `__lt__` function of your class, or multiply the values you're adding by -1; thus the elements you heappop will be the `largest` after you. 
# Alternatively there's also the following. '_heappush_max' function.

max_heap = []
heapq._heappush_max(max_heap, Person("Ann", '16'))
heapq._heappush_max(max_heap, Person("Bob", 14))
heapq._heappush_max(max_heap, Person("Sam", 12))
heapq._heappop_max(max_heap) # ("Sam", 12)