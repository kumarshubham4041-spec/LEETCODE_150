# Question : Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
# Approach : I used a counting array to avoid sorting, then iterated from the highest possible h-index downward while maintaining a cumulative count of papers to find the maximum h such that at least h papers have ≥ h citations.
# Time Complexity : O(n)
# Space Complexity: O(n)


def hIndex(self, citations: List[int]) -> int:
        n= len(citations)
        result= [0]*(n+1)

        for c in citations:
            result[min(c,n)] += 1

        h = n
        count = result[n]

        while count < h:
            h-= 1
            count += result[h]

        return h
