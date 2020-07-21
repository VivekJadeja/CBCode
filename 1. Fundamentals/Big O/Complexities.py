#How to Analyze Algorithms

#We have a sorted list of integers. I want to know some target, x, is in the list.
from stopwatch import Stopwatch
import random
# [1,2,3,4,5,6,7,8] look for  3.

# Approach 1: Search starting from the front. Check if every single number is the target
# LINEAR SEARCH IS FASTER IF OUR TARGET IS AT THE BEGINNING OF THE LIST
# Search 1,2,3 found target 3 and return True

# [1,2,3,4,5,6,7,8] look for  9.
# We would be looking all through the list and see 9 isn't in the list and return False.

# Approach 2: Binary Search - Continue cutting the list in half until we find our target
# BINARY SEARCH IS FASTER IF THE TARGET IS NOT IN THE LIST OR IS NEAR THE END OF THE LIST
# [1,2,3,4,5,6,7,8] look for  3.
# First look in middle at 4, then look at left half from 1-4, then find other midpoint which is 2.
# Then we would see that 3 > 2, so we will between 2 and 4 and see it is 3, so return True

# [1,2,3,4,5,6,7,8] look for  9.
# Same thing to look for 9. 4  is the midpoint. Look from 4-8. Next midpoint would be 6, then 7, then look at 8. False

#---------------------------------------------------------------------------------------------------------------------------
# HOW LONG WILL MY PROGRAM TAKE TO RUN? (Time Complexity)
# HOW MUCH MEMORY WILL I USE? (Space Complexity)

# These are normally approximations based on input size

# WHAT WILL HAPPEN WHEN INPUT INCREASES?

# Common Orders of growth from fastest to slowest (lowest number of operations vs highest)

#   Constant: O(1)
#   Fixed number of iterations or operations. Does not depend on input size
def constant_run_time(N):
    total_sum = 0
    for i in range(0,50): # Constant run time because it will run 50 times. It is not based on N
        total_sum += i
    return total_sum

#   Logarithmic O(log n)
# if n = 16, then it will be 4. 2^4 = 16
# It means as you double the inputsize, you would expect this kind of relationship
# N     Runtime
# 2     1
# 4     2
# 8     3
# 16    4
#   For or while loop incrementing at *2
def log_run_time(N):
    i = 1
    total_operations = 0
    while i < N:
        total_operations += 1
        i *= 2
    return total_operations

#   Linear Runtime O(n)
#   1 to 1 change, for input size to runtime (number of operations)
#   Single for loop iterating
def linear_run_time(N):
    total_operations = 0
    i = 1
    while i < N:
        total_operations += 1
        i += 1
    return total_operations

#   Quadratic Runtime O(N^2)
#   As we double N, the runtime(nuber of ops) is multiplied by 4, so N^2
#   Double for loop
def quadratic_run_time(N):
    i = 1
    total_operations = 0
    while i < N:
        j = 1
        while j < N:
            total_operations += 1
            j += 1
        i += 1
    return total_operations

#   Linearithmic O(n log n)
#   You have a for loop iterating and you also have another for loop that's incrementing by *2
def linearithmic_run_time(N):
    i = 1
    total_operations = 0
    while i < N:
        j = 1
        while j < N:
            j = j * 2
            total_operations += 1
        i += 1
    return total_operations

#   Exponential O(2^n) for each input increase by 1, it will double the runtime (number of operations). Insanely slow
#   Multiple recursive calls
def exponential_run_time(N):
    if N == 0:
        return 1
    total_operations = 0
    total_operations += exponential_run_time(N-1)
    total_operations += exponential_run_time(N-1)
    return total_operations


#if __name__ == "__main__":
#    input_sizes = [12, 13, 14, 15, 16, 17, 18]
#    for input_size in input_sizes:
#        timer = Stopwatch()
#        total_operations = exponential_run_time(input_size)
#        print(input_size, total_operations, timer.elapsed_time())


# Constant O(1)
# Logarithmic O(log n)
# Linear O(n)
# Linearithmic O(n log n)
# Quadratic O(n^2)
# Exponential O(2^n)

# EXAMPLES
# 2 log n BECOMES O(log n)

# 2 log n ~ 10 log n ~ 10000 log n ~ .00001 log n
# We only care about the order of growth for the largest terms, so these constants don't matter

# 50 n^2 + 10 n log n
# This becomes O(n^2) because that is the largest term. This allows us to analyze without worrying about constants and smaller terms.
# If you have the largest term, it makes it easier to discuss and thing about big picture ideas.

# To answer the question from the beginning to look for the target, we will code the approaches
#We have a sorted list of integers. I want to know some target, x, is in the list.
# Approach 1: Search starting from the front. Check if every single number is the target
# Gives proportional 1 to 1 increase with input size and output/runtime/number of operations - O(n) runtime
def approach_one(our_list, target):
    for i in range(0, len(our_list)):
        number = our_list[i]
        if number == target:
            return i
    return -1

# This approach is faster because it has O(log n) runtime
def approach_two(our_list, target, lo, hi):
    #as long as the higher index > lower index
    if hi >= lo:
        mid = lo + (hi - lo) // 2

        #if element is in the middle
        if target == our_list[mid]:
            return mid
        
        #if element is smaller than mid, then take the left half and search it
        elif target < mid:
            return approach_two(our_list, target, lo, mid-1)
        
        #if element is > mid, search right subarray
        elif target > mid:
            return approach_two(our_list, target, mid+1, hi)

    else:
        return -1

if __name__ == "__main__":
    input_sizes = [5, 10, 20, 40]
    num_samples = 100
    for x in input_sizes:
        input_size = 2 ** x
        timer = Stopwatch()
        input_list = range(0, input_size)
        total_runtime = 0
        for i in range(0, num_samples):
            target = random.randint(0, input_size)
            approach_two(input_list, target, 0, input_size-1)
            total_runtime += timer.elapsed_time()
        print(input_size, timer.elapsed_time() / num_samples)