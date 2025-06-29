class Solution:
    def mySqrt(self, x: int) -> int:

        l=0
        r=x//2+1
        ans=1
        while l<=r:
            m=(l+r)//2
            if m*m==x:
                return m
            if m*m<=x:
                l=m+1
            else:
                r=m-1
        return l-1