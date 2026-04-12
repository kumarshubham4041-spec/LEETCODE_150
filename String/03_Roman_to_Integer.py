# Question : Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:I can be placed before V (5) and X (10) to make 4 and 9. X can be placed before L (50) and C (100) to make 40 and 90. C can be placed before D (500) and M (1000) to make 400 and 900.Given a roman numeral, convert it to an integer.
# Approach : I iterated the elements of string s and compared each element with the element coming next .If the current element is small i subtracted current element from sum which is initially 0 and if current element is bigger than next element then i added current element in the sum.
# Time Complexity : O(n)
# Space Complexity : O(1) 

    def romanToInt(self, s: str) -> int:
        res = {"I":1, "V":5 , "X": 10, "L":50,"C":100,"D":500,"M":1000}
        n= len(s)
        summ = 0
        for i in range(n):
            if i<n-1 and res[s[i]]<res[s[i+1]]:
                summ -= res[s[i]]
            else :
                summ+= res[s[i]]

        return summ
