# Question : Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Time Complexity :   O(n*m) where n = length of list and m =  length of string

# Space Complexity : O(n)


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= defaultdict(list)

        for i in range(len(strs)):
            count = [0]*26
            for c in strs[i]:
                count[ord(c)-ord('a')] += 1
            #Tuple(count) is used as key of hashmap cant't be mutable
            res[tuple(count)].append(strs[i])

        return list(res.values()) 
