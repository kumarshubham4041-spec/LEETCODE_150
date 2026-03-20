# Question: In this question we have to ramove dduplicates from sorted array in place such that any elements appears only twice and the order of the elements is maintained.
# Approach : I have applied two pointer technique which move in the same direction . Firstly i compared present element with the element two places before. if it matches, then this element has appeared thrice so it is replaced by the next new element.
#Time Complexity : O(n)
# Space Complexity : O(1)

def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2: 
            return len(nums)

        k=2
        for i in range(2,len(nums)):
            if nums[i]!= nums[k-2]:
                nums[k]=nums[i]
                k+= 1
        return k
