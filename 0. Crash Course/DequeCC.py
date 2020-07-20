from collections import deque

d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
  print(elem.upper())

d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side
print(d)                         # show the representation of the deque

# return and remove the rightmost item
popped =  d.pop() # 'j'
print(popped)

# return and remove the leftmost item
popped = d.popleft() # 'f'
print(popped)

# peek at leftmost item
d[0] # 'g'

# peek at rightmost item
d[-1]  #'i'

# list the contents of a deque in reverse
list(reversed(d)) # ['i', 'h', 'g'] 

# Check if 'h' is in the deque. This takes O(n) time.
print('h' in d)  #True

d.extend('jkl')                  # add multiple elements at once
print(d)

d.rotate(1)                      # right rotation
print(d)

d.rotate(-1)                     # left rotation
print(d)

print(deque(reversed(d)))             # make a new deque in reverse order

d.clear()                        # empty the deque

d.pop()                          # cannot pop from an empty deque

d.extendleft('abc')              # extendleft() reverses the input order
print(d) # deque(['c', 'b', 'a'])