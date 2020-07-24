for x in range(n):
    pass
    # statement(s) that take constant time
#Running Time Complexity = n = O(n)

# For-loop with Increments #
for x in range(1, n, k):
    pass
    # statement(s) that take constant time
# Runing Time Complexity = floor(n divided by k) = O(n)

# Simple Nested For-loop #
for i in range(n):
    for x in range(m):
        pass
        # Statement(s) that take(s) constant time
# Running Time Complexity = n * m =O(n*m)

# Nested For-loop with Dependant Variables #
for i in range(n): # outer loop runs n times
    for x in range(i): # Inner loop runs (n-1)/2 times for each n, so total TC is O((n*(n-1))/2)
        pass
        # Statement(s) that take(s) constant time
​# O(n^2) Running Time Complexity

# Nested For-loop with Index Modification #
for i in range(n):
    i *= 2
    for x in range(i):
        pass
        # Statement(s) that take(s) constant time
#Running Time Complexity = n(n-1) = n^2-n = O(n^2)
​
i = 1#constant
n = 1#constant
k = 1#constant
while i < n:
    i*=k
    # Statement(s) that take(s) constant time
# Running Time Complexity = O(log base k (n))


n = 10  # Can be anything
sum = 0
pie = 3.14
var = 1
while var < n: # Ececutes O(log n) times
    print(pie) # Executes O(log n) times
    for j in range(var): #total for loop iterations: runs 2^(k+1)-1 times because every time var doubles, so does the range here. 2^0 + 2^1 + 2^2 + 2^3 = 1 + 2 + 4 + 8 = 15 
        sum += 1                            # 2^k < n, since we know the last value of var has to be less than n.
    var *= 2 #executes O(log n) times       # we can apply log2() to both sides, log(2^k) < log(n) -> k < log(n) since log(2^k) = k
print(sum)                                  # Now that we have k < log(n) we know that k is in O(log(n))
                                            # The for loop iterates 2^k times, so replace k with log(n)
                                            # 2^(log(n)+1) - 1 gives us 2n-1 -> Thus, the time complexity is O(n)
# This is hard to understand, but we can just say that the while loop with O(log n) with a for loop depending on the var of the while loop
# that is changing iterates 2^(k+1)-1 times and we can plug in log(n) for k and we get 2n-1 so it is O(n) run time


n = 10  # n can be anything, this is just an example
sum = 0
pie = 3.14
var = 1
while var < n: # While loop iterates log_3(n) times
    print(pie) # This statemennt executes log_3(n) times
    for j in range(1, n, 2): #Iterates n/2 times per each iteration of the while loop which iterated log_3(n) times
        sum += 1             #Therefore, the for loop and its contents iterate O((n/2)log_3(n)) times
    var *= 3 # This statement executes log_3(n) times
print(sum) #Executes once
# Total Run Time Complexity: O(1) + O(1) + O(1) + O(1) + O(log_3(n)) + O(log_3(n)) + (log_3n * n/2) + (log_3n * n/2) + log_3(n) + O(1)
# These added up gives us: 2(n log_3(n)) + 3(log_3(n)) + 5(1) = O(n log_3(n))
# And log_3(n) = log_2(n) / log_2(3) = log_2(n) / 1.585 -> dropping constants gives us O(log_2(n))

n = 10  # can be anything, this is just an example
sum = 0
pie = 3.14
for var in range(1, n, 3): # Iterates n/3 times
    j = 1 # Iterates n/3 times
    print(pie) # Iterates n/3 times
    while j < n: # Iterates log_3(n) times for each iteration of the while loop, so n/3 * log_3(n) times
        sum += 1 # Iterates n/3 * log_3(n) times
        j *= 3   # Iterates n/3 * log_3(n) times
print(sum)  # O(1)
# Total TC: 3 O(n/3) + 3 O(n/3 * log_3(n)) = O(n) + O(n * log_3(n)) = O(n * log_3(n))
# but with log_3(n) = log_2(n)/log_2(3) = log_2(n) / 1.585 -> log_2(n)
# So O(n * log_2(n)) is total TC



n = 10  # can be anything
sum = 0
pie = 3.14
for i in range(n): # Iterates n times
    j = 1
    while j < i: # Iterates once for i=2, twice for i=3,4, 3 times for i=5-8, 4 times for i=9
        sum += 1 # This pattern is ciel(log_2(2)) = 1 iteration, ciel(log_2(3)) = 2 iteration, ciel(log_2(4)) = 2 iteration, ciel(log_2(5)) = 3, ciel(log_2(9)) = 4
        j *= 2   # Which means it's summation of log_2(index) from i to n. which is log_2(n!)
    print(sum)
# Total Time Complexity: This means that the total time complexity of this is O(n * log_2(n!)) which is the tight upper bound
#                        This can be converted to a loose upper bound of O(n * log_2(n))



n = 10  # can be anything
sum = 0
pie = 3.14
j = 1
for var in range(n): # n iterations
    while j < var:   # NO IDEA why this is O(n), but it is. Just memorize it
        sum += 1
        j *= 2
    print(sum)
# TC: O(n)

