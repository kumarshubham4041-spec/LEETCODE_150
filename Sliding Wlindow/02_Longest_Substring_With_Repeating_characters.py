# Question : Given a string s, find the length of the longest substring without duplicate characters.
# Time Complexity : O(n)
# Space Complexitty : O(1)

    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        i= 0
        maxLength = 0
        for j in range (len(s)):
            while s[j] in charset:
                charset.remove(s[i])
                i+= 1
            charset.add(s[j])
            maxLength = max(maxLength , j-i+1)

        return maxLength 
