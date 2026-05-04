# Question : Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:Starting with any positive integer, replace the number by the sum of the squares of its digits.Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.Those numbers for which this process ends in 1 are happy.Return true if n is a happy number, and false if not.

# Time Complexity : O(n)

# Space Complexity : O(n)

    def isHappy(self, n: int) -> bool:
        numbSet= set()
        while n not in numbSet:
            numbSet.add(n)
            n = self.sumofSquares(n)
            if n== 1:
                return True
        return False

    def sumofSquares(self,n: int)-> int:
        res= 0
        while n:
            digit = n%10
            digit = digit **2
            res += digit
            n//= 10
        return res
