# Question : Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.

# Time Complexity : O(n)

# Space Complexity : O(n)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in index_map:
                return [index_map[complement],i]
            index_map[nums[i]]= i
