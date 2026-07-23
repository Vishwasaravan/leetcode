class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=sorted(heights)
        length=len(heights)
        output=0
        for i in range(length):
            if heights[i]!=expected[i]:
                output=output+1
        return output