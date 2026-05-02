class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        if length == 1:
            return cost[0]
        dp = [0] * (length + 1)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, length):
            dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])

        dp[length] = min(dp[length - 1], dp[length - 2])
        
        return dp[length]