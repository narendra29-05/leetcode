class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x//2+1 #---->because the square root value always less then x//2+1 
        
        while l<=r:
            m=(l+r)//2
            if m*m==x:
                return m
            if m*m>x:
                r=m-1
            if m*m<x:
                l=m+1
        return l-1
        