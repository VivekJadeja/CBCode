def twoSum(self, nums, target):
    #create a hashmap
    map = {}
    for i, value in enumerate(nums):
        if target-value in map:
            return map[target-value], i
        else:
            map[value] = i
