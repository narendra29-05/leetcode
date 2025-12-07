from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        # Find the first positive number index
        l, r = 0, n - 1
        while l<=r:
            m=(l+r)//2
            if nums[m]>=0:
                r=m-1
            else:
                l=m+1
        z=nums.count(0)
        print(z,l)
        return max(l,n-l-z)
