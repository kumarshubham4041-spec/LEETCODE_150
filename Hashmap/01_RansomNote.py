# Question : Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.Each letter in magazine can only be used once in ransomNote.
# Time Complexity : O(n)
# Space Complexity : O(n)

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequency = {}
        for ch in magazine:
            frequency[ch] = frequency.get(ch,0)+1
        
        for ch in ransomNote:
            if frequency.get(ch,0)== 0:
                return False
            frequency[ch]-= 1
        
        return True
