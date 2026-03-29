# Question : There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.
# Approach : I use a greedy approach. First, I check if completing the circuit is possible by comparing total gas and total cost. If total gas is less than total cost, it's impossible to complete the circuit, so I return -1.Otherwise, I iterate through the stations while maintaining a running balance (currentGain). If at any point the balance becomes negative, it means we cannot start from the current starting index, so I reset the start to the next station and reset the balance.At the end, the last updated start index is the valid starting point.
# Time Complexity : O(n)
# Space Complexity : O(1)

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas = 0
        totalCost = 0
        currentGain = 0
        start=0
        for i in range(len(gas)):
            totalGas += gas[i]
            totalCost += cost[i]
            currentGain += gas[i]-cost[i]
            if currentGain< 0:
                start= i+1
                currentGain = 0
        if totalCost>totalGas:
            return -1
        else:
            return start
