# Question : You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:0 <= j <= nums[i] and i + j < n Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.
# Approach : I solve this using a greedy approach. I maintain a range of indices reachable with the current number of jumps. While iterating, I compute the farthest index I can reach. When I reach the end of the current range, I increment the jump count and update the range to the farthest reachable index. This ensures minimum jumps in O(n) time
# Time Complexity : O(n)
# Space Complexity : O(1)

    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        reach= 0
        end= 0
        steps= 0
        for i in range(len(nums)-1):
            reach= max(reach,i+nums[i])
            if i== end:
                steps+= 1
                end = reach
            
        return steps
