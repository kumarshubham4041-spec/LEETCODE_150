# Question : Given a string s consisting of words and spaces, return the length of the last word in the string.A word is a maximal substring consisting of non-space characters only.
# Approach : I used a pointer to traverse through characters in string. Firstly i used a for loop to traverse through trailing spaces. Then i used a lenght variable and traversed through array to count length of last word .
# Time Complexity : O(n)
# Space Complexity : O(n)

    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1

        while i>=0 and s[i]== ' ':
            i-=1

        length = 0
        while i>= 0 and s[i]!= ' ':
            length += 1
            i -= 1
        
        return length
