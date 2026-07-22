class Solution:
    def climbStairs(self, n: int) -> int:
        d={}
        def x(n):
            if n<=2:
                return n
            if n not in d:
                d[n]=x(n-1)+x(n-2)
            return d[n]
        return x(n)