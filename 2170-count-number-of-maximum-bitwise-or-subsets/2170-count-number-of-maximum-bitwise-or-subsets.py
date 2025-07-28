from collections import defaultdict
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or=0
        for i in nums:
            max_or|=i
        count=0
        def maxb(i,cur):
            nonlocal count
            if i==len(nums):
                if max_or==cur:
                    count+=1
                return
            maxb(i+1,cur|nums[i])
            maxb(i+1,cur)
        maxb(0,0)
        return count