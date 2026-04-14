    def convert(self, s: str, numRows: int) -> str:
        if numRows== 1:
            return s
        res = ""
        for i in range(numRows):
            increment = 2*(numRows - 1)
            for r in range(i, len(s),increment):
                res += s[r]
                if (i>0 and i<numRows-1 and r + increment-2*i< len(s)):
                    res += s[r+ increment-2*i]

        return res
