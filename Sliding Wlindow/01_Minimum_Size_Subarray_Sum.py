# Question : Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# Time Complexity : O(n)
# Space complexity : O(1)

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        summ = 0
        count = float('inf')
        for j in range(len(nums)):
            summ+= nums[j]
            while summ>= target :
                count = min(count,j-i+1)
                summ-= nums[i]
                i+= 1

        if count == float('inf'):
            return 0
        return count
