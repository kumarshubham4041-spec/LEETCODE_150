# Question : Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Time Complexity : O(n)
# Space Complexity : O(1)


    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        leftMax = height[i]
        rightMax = height[j]
        result = 0
        while i < j:
            if leftMax <= rightMax :
                i += 1
                leftMax = max(height[i],leftMax)
                result += leftMax - height[i]

            else:
                j-= 1
                rightMax = max(height[j],rightMax)
                result += rightMax - height[j]

        return result
