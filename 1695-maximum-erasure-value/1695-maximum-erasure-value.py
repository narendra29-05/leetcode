class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left=right=0
        d=defaultdict(int)
        sum1=0
        f_sum=0
        while right<len(nums):
            d[nums[right]]+=1
            sum1+=nums[right]
            while d[nums[right]]>1:
                d[nums[left]]-=1
                
                sum1-=nums[left]
                left+=1
            f_sum=max(sum1,f_sum)
            right+=1
        return f_sum
