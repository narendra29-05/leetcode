class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        d=Counter(nums)
        c=second=0
        print(d)
        for i in d:
            if i>=k:     
                
                second+=d[i]
        return len(nums)-second
