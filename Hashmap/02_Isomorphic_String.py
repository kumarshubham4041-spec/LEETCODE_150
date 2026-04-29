# Question : Given two strings s and t, determine if they are isomorphic.Two strings s and t are isomorphic if the characters in s can be replaced to get t.All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
# Time Complexity : O(n)
# Space Complexity : O(n)

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        maps_t = {}
        mapt_s = {}

        for i in range(len(s)):
            if s[i] in maps_t:
                if maps_t[s[i]]!= t[i]:
                    return False
            else :
                maps_t[s[i]]= t[i]

            if t[i] in mapt_s:
                if mapt_s[t[i]]!= s[i]:
                    return False
            else:
                mapt_s[t[i]]= s[i]

        return True
