# Question : Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.The tests are generated such that there is exactly one solution. You may not use the same element twice.Your solution must use only constant extra space.
# Approach : I used two pointer approach keeping both pointers at first and last index respectively . Then i calculated sum of eleenets at ech piinter location . If sum was equal to target i returned both pointers after increasing their value by 1 as answer must be returned in 1 index format. If the sum was small i increased left pointer by 1 and if sum was greater than target i reduced right pointer by 1.
# Time Complexity : O(n)
# Space Complexity : O(1)

    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j= 0
        seen=[]
        while i<len(s) and j<len(t):
            if s[i]== t[j]:
                seen.append(s[i])
                i+=1
                j+= 1
            else :
                j+= 1
        
        if len(seen)== len(s):
            return True
        else :
            return False
