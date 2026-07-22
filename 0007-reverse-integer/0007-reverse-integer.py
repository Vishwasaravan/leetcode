class Solution:
    def reverse(self,x:int) ->int:
        z=x
        r=0
        if x<0:
            x*=-1
        while x!=0:
            h=x%10
            r=r*10+h
            x//=10
        if z<0:
                r*=-1
        if -2**31<r<2**31-1:
             return r
        else:
            return 0
         

        
        
        