# Question : Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Time complexity : O(n)
# Space Complexity : O(n)

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        map_st = {}
        map_ts = {}
        for i in range(len(s)):
            if map_st.get(s[i],0)== 0:
                map_st[s[i]] = 1
            else:
                map_st[s[i]]+= 1

            if map_ts.get(t[i],0)== 0:
                map_ts[t[i]] = 1
            else:
                map_ts[t[i]]+= 1


        for ch in t: #can also use ch in map_st and then get will apply in map_ts
            if map_st.get(ch,0)!= map_ts[ch]:
                return False
        return True
