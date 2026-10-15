class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = []

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    arr.append(prices[j] - prices[i])

        if len(arr) == 0:
            return 0

        return max(arr)  