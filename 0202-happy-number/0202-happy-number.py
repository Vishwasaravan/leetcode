class Solution:
    def isHappy(self, n: int) -> bool:
        x=0
        l=[0]
        while True:
            z=n%10
            n//=10
            x+=z**2
            if n==0:
                if x in l:
                    return False
                if x==1:
                    return True
                l.append(x)
                n=x
                x=0

