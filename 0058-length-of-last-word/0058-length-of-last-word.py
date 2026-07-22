class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=s.split()
        x=len(l[-1])
        return x
        