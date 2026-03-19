# Question : In this question , we have to return the majority element which appears more than [n/2] times in an array of size n.
# Approach : In this question i have maintained two variables one for majority element and one for keeping its count . whenever same element appears its count increases and when other element appears , previous elements' count decreases . when count becomes 0 majority element changes and its count increase . This process continues until majority element is found.
# Time Complexity : O(n)
# Space Complexity : O(1)

def majorityElement(self, nums: List[int]) -> int:
        majorEle = None
        count= 0
        for num in nums:
            if count== 0:
                majorEle= num
                count+=1
            elif num== majorEle:
                count+=1
            else:
                count-=1
        
        return majorEle
