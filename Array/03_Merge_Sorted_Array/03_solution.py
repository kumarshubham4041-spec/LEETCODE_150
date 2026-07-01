# Question :IN this question we are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.Merge nums1 and nums2 into a single array sorted in non-decreasing order.The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# Approach : Two pointer approach is applied to solve this problem . One pointer is kept at m-1 and one at n-1 .Both the elements of both arrays are compared and whichever element is found bigger is placed at the end of first array .This process continues until all the elements are placed .
# Time Complexity : O(m+n)
# Space Complexity : O(1)

index= m+n-1
i= m-1
j=n-1
while i>=0 and j>=0 :
    if nums1[i]>nums2[j]:
       nums1[index]=nums1[i]
       i-=1
       index-=1
    elif nums1[i]<=nums2[j]:
       nums1[index]= nums2[j]
       j-=1
       index-=1
while j>=0:
     nums1[index]= nums2[j]
     j-=1
     index-=1
