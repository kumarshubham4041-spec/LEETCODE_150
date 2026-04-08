# Question : Given an input string s, reverse the order of the words.A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.Return a string of the words in reverse order concatenated by a single space.Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
# Approach : Firstly i reversed all characters of the string . Then i created an empty string ans. Then i started iteration from i= 0 and added each string of words to empty string word until a space is found.Then i again revcersed characters of word and added it to ans string wuth empty space. Then again i is incremented by 1 place to avoid space .This continues until all characters of string is iterated and then ans string is returned with strip method to remove extra spaces from start.
#Time Complexity : O(n)
# Space Complexity : O(n)

    def reverseWords(self, s: str) -> str:
        s= s[::-1]
        n  = len(s)
        ans = " "
        i = 0
        while i<n:
            word = ""
            while i<n and s[i]!= " ":
                word += s[i]
                i+= 1
            word = word[::-1]
            if len(word)>0:
                ans+=" "+ word

            i += 1
        return ans.strip()
