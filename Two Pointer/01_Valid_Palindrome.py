# Question : A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.Given a string s, return true if it is a palindrome, or false otherwise.
# Approach : Firstly i declared two pointers at start and end of string. Then i started iterating until pointers cross each other . I called alphanumeric function to check if current element at both pointers are alphanumeric or not .If they are not i moved the pointers until alphanumeric element is found. Then i checked if elements at both pointers are equal or not . If not then i returned false  and if they are eaqual i moved my pointers until the end of loop. At last i returned True indicating given string is a palindrome.
# Time Compolecity : O(n)
# Space Complecity : O(1)

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<j:
            if not self.isAlphanumeric(s[i]):
                i += 1
                continue
            if not self.isAlphanumeric(s[j]):
                j-= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1 
            j-= 1
        return True
    
    def isAlphanumeric(self ,c):
        if (c.lower() >= "a" and c.lower()<= "z") or (c.lower() >= "0" and c.lower()<= "9"):
            return True
        return False
