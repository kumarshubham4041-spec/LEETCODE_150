# Question : Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
# Approach : Two pointer technique is used in this question to compare new element with the preceding element . If the new element is different from previous element then we swap its places with the previous duplicate element .This process continues until all the k unique elements are places in first  k places of the array.
# Time Complexity : O(n)
# Space Complexity : O(1)

    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1,len(nums)):
            if nums[i]!= nums[k-1]:
                nums[k]= nums[i]
                k+= 1
        return k
