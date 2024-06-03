""" 
You are given an integer array const where cost[i] is the cost of ith step on staircase. Once you play the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1

Return the mininum cost to reach the top of the floor

Example 1:
input: cost = [10, 15, 20]
output: 15
explanation: You will start at index 1. -Pay 15 and climb two steps to reach the top. The total cost is 15.
"""

def minCostClimbingStairs(cost: list[int]) -> int:
    n = len(cost)
    # panjang nilai dari cost
    prev, curr = 0, 0
    # menyimpan variable dari tangga sebelumnya dan tangga saat ini

    for i in range(2, n + 1):
        prev, curr = curr, min(cost[i - 2] + prev, cost[i - 1] + curr)
    
    return curr
   

print(minCostClimbingStairs([1, 100, 1,1,1,100,1,1,100,1]))
    
