# Greedy Algorithm solves a problem by building a solution incrementally
# The algorithm is greedy because it chooses the next step that gives the most benefit
# Can save a lot of time when used correctly since they don't have to look at the entire problem space
# It's either the most optimal solution or it doesn't work at all, so you have to know for sure when to use it
# It's a short-sighted algorithm since we are only looking to optimize the input, not the entire solution

# Problem 1 JUMP GAME

# given an array of non-negative integers, we are starting at the first index of the array
# each element in the array represents our maximum jump length at that position
# determine if we can reach the last index
# this stands out as a greedy algorithm

#ex. [2,3,1,1,4]
#   true since we can go from 2 to 3 to 4, or 2 to 1 to 1 to 4

class Solution:
    #O(n) runtime b/c iterating through array
    #O(1) SC b/c no extra space taken up
    def canJump(self, nums):
        best_index = 0
        # for each index in the array
        for i in range(len(nums)):
            # if the current index is greater than the best index
            if i > best_index:
                return False
            # the best index will become the maximum between the best index and the number at the current index + the current index
            best_index = max(best_index, nums[i] + i)
        return True

if __name__ == "__main__":
    ok = Solution()
    ans = ok.canJump([2,3,1,1,4])
    print(ans)

