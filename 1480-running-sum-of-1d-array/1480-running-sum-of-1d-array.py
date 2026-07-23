class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        resalt =[]
        tot=0
        for i in nums:
            tot=tot+i
            resalt.append(tot)
        return resalt 
        