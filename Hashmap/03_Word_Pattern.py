# Question : Given a pattern and a string s, find if s follows the same pattern.Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:Each letter in pattern maps to exactly one unique word in s.Each unique word in s maps to exactly one letter in pattern.No two letters map to the same word, and no two words map to the same letter.
# Time Complexity : O(n)
# Space Complexity : O(n)

    def wordPattern(self, pattern: str, s: str) -> bool:
        map_st = {}
        map_ts = {}
        j = 0
        for i in range(len(pattern)):
            if j >= len(s):
                return False
            word= ""
            while j<len(s) and s[j]!= " ":
                word += s[j]
                j+= 1

            if pattern[i] in map_st:
                if map_st[pattern[i]]!= word:
                    return False
            else:
                map_st[pattern[i]] = word
            
            if word in map_ts:
                if map_ts[word]!= pattern[i]:
                    return False
            else:
                map_ts[word]= pattern[i]
            j+= 1

        if j < len(s):
            return False
        return True

