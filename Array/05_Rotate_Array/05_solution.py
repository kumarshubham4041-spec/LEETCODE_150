# Question : Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Approrach : I rotated the array by reversing the whole array first, then reversing the first k elements and the remaining elements to get the final rotated array
# Time Complexity : O(n)
# Space Complexiyt : O(1)

def rotate(self, nums: List[int], k: int) -> None:
        n= len (nums)
        if n==0:
            return 
        k= k%n
        def reverse(left,right):
            
            while left<right:
                nums[left],nums[right]= nums[right],nums[left]
                left += 1
                right-= 1
        
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
