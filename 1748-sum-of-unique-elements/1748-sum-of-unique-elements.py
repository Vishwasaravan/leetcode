class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        l=sum(i for i in nums if nums.count(i)==1)
        return l
        