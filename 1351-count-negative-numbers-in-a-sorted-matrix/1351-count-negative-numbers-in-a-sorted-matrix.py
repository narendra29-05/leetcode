class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def check(array):
            l=0
            r=len(array)-1
            neg=len(array)
            while l<=r:
                m=(l+r)//2
                if array[m]>=0:
                    l=m+1
                else:
                    neg=m
                    r=m-1
            return len(array)-neg
        ans=0
        for array in grid:
            ans+=check(array)
        return ans

