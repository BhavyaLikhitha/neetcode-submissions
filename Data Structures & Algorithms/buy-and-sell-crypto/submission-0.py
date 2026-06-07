class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        mi = prices[0]
        for s in prices:
            mx = max(mx, s-mi)
            mi = min(mi, s)
        return mx