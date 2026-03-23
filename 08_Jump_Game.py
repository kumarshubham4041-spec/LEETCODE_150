# Question : You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.Return true if you can reach the last index, or false otherwise.
# Approach : I use a greedy approach where I track the farthest index I can reach while iterating. If at any point the current index exceeds this reach, it means it's not reachable, so I return false. If I complete the traversal, it means I can reach the last index.
# Time Complexity : O(n)
# Space Complexity : O(1)

    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if i >reach:
                return False
            reach= max(reach,i+nums[i])
        
        return True
