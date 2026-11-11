class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        steps = 0
        while any(gt(*p) for p in pairwise(nums)):
            i, m = min(enumerate(starmap(add, pairwise(nums))), key = itemgetter(1))
            nums[i] = m
            del nums[i+1]
            steps += 1
        return steps