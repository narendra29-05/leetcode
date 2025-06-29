class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        first=len(nums)
        while l<=r:
            m=(l+r)//2
            if nums[m]>=target:
                first=m
                r=m-1
            else:
                l=m+1
        return first 