# Question : There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.You are giving candies to these children subjected to the following requirements:Each child must have at least one candy.Children with a higher rating get more candies than their neighbors.Return the minimum number of candies you need to have to distribute the candies to the children.
# Approach : I traverse ratings once, identifying increasing and decreasing slopes. I assign candies incrementally for both slopes and adjust when the decreasing slope is longer than the increasing one to satisfy constraints. This gives an O(n) time and O(1) space solution
# Time Complexity : O(n)
# Space Complexity : O(1)

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        sum= 1
        i = 1
        while i<n:
            if ratings[i]== ratings[i-1]:
                sum += 1
                i+= 1
            peak = 1
            while i<n and ratings[i]>ratings[i-1]:
                peak += 1
                sum += peak
                i+= 1
            down = 1
            while i<n and ratings[i]<ratings[i-1]:
                sum+=  down
                i+= 1
                down+= 1
            
            if down>peak:
                sum+= down-peak
        return sum
