class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        pref=[]
        value=0
        for i in nums:
            value+=i
            pref.append(value)
        c=0
        for i in pref:
            if abs(value-2*i )%2==0:
                c+=1
        return c-1 if c else c
