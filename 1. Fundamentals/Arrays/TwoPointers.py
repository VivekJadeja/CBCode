# On problems with string or arrays where we need to choose a range or simply 2 points in the string of index of an array
# to optimize a certain value, you want to use a two pointer approach

# Two pointers i and j to reference indices. i = 0 most of the time and then j will either be 1(i) or N(end)
# depending on the problem.

# For now we will assume j = 1. As we iterate, we will evaulate the object function and either increment i or increment j as needed while maintaining
# the indices of the previous optimal solution

# CONTAINER WITH MOST WATER PROBLEM - We are given n non-negative integers a_1, a_2,..., a_n where each one represents a point at coordinate (i, a_i).
# n vertical lines are drawn such that the two endpoints of line i is at (i, a_i) and (i, 0).

# We are looking for two lines which together with x-axis forms a container, such that the container contains the most water.


# Vivek's Thoughts: So essentially, i is the index and it will be the position on the x-axis of the vertical line.
#                   whereas a_i is the y coordinate. so given (i, a_i) this would give us the coordinate on x-y plane.

# For this problem's sake, the array will be [1,8,6,2,5,4,8,3,7]
# In this case, the maximum amount of water that the water can contain is 49

# Start one pointer at the front and one at the end
# we will calculate the first distance

#        P               P
# arr = [1,8,6,2,5,4,8,3,7]
def most_water(arr):
    # making sure that there are at least 2 numbers in the array
    # Edge case that length is at least 2
    if len(arr) < 2:
        return -1
    start = 0
    end = len(arr) - 1
    max_product = float('-inf')

    #O(n) time complexity because the while loop is iterating through the array
    #O(1) space complexity because we aren't storing anything additional. We are just using pointers
    while start < end:
        # taking the minimum of the start and end, meaning that we are taking the shortest vertical line
        # then we multiply it by the distance between the two lines
        product = min(arr[start], arr[end]) * (end - start)
        # update the max product to equal the max
        max_product = max(max_product, product)
        if arr[start] < arr[end]:
            start +=  1
        else:
            end -= 1
    return max_product

arr = [1,40,6,2,5,4,40,3,7]

print(most_water(arr))