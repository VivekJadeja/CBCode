class Solution:
    #O(n) TC and O(1) SC since we are iterating through each element and not using any extra space
    def findNumbers(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                sum += 1
        return sum