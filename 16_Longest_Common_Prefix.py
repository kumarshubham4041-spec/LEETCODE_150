# Question : Write a function to find the longest common prefix string amongst an array of strings.If there is no common prefix, return an empty string ""
# Approach : I take the first string as a reference prefix. Then I compare this prefix with every other string in the array.If the current string does not start with the prefix, I keep reducing the prefix by removing its last character.I repeat this process until the prefix matches the beginning of the current string.If at any point the prefix becomes empty, I return an empty string. Otherwise, after checking all strings, the remaining prefix is the longest common prefix
# Time Complexity : O(n*m)
# Space Complexity : O(1)

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return " "
        prefix = strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(prefix)!= 0:
                prefix= prefix[:-1]

        return prefix
