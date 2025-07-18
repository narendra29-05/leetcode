class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c=1
        ans=0
        even=odd=0
        for i in nums:
            if i%2==0:
                even+=1
            if i%2==1:
                odd+=1
            if i%2==0 and c==1:
                c=0
                ans+=1
            elif c==0 and i%2==1:
                c=1
                ans+=1
        c=1
        ans1=0
        for i in nums:
            if i%2==1 and c==1:
                c=0
                ans1+=1
            elif c==0 and i%2==0:
                c=1
                ans1+=1
        print(even,odd,ans,ans1)
        return max(even,odd,ans,ans1)
                
