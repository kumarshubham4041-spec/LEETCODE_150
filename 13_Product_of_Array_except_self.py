# Question : Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.You must write an algorithm that runs in O(n) time and without using the division operation.
# Approach : I declared an attay answer of size n .Then i used prefix and suffix product to store product of values before nums[i] in answer then multiplying it with product of elements after nums[i].
# Time Complexity : O(n)
# Space Compleity : O(n)

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer= [1]*n

        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        right = 1
        for i in range(n-1,-1,-1):
            answer[i] *= right
            right *= nums[i]

        return answer
