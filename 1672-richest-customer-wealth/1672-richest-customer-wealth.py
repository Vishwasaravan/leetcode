class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=0
        for i in accounts:
            wealth=sum(i)
            maxi=max(maxi,wealth)
        return maxi
        