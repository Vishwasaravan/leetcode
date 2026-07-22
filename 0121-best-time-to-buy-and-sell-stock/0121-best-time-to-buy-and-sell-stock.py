class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x=prices[0]
        y=0
        for i in prices:
            if i<x:
                x=i
            elif i-x>y:
                y=i-x
        return y
        