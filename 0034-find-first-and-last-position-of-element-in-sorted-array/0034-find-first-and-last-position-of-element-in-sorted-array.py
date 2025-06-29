from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r=0,len(nums)-1
        first=len(nums)
        while l<=r:
            m=(l+r)//2
            if nums[m]>=target:
                r=m-1
                first=m
            else:
                l=m+1
        if first==len(nums) or nums[first]!=target :
            return [-1,-1]
        l,r=0,len(nums)-1
        last=len(nums)
        while l<=r:
            m=(l+r)//2
            if nums[m]>target:
                r=m-1
                
            else:
                last=m
                l=m+1
        return [first,last]

