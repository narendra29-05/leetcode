class Solution:
    def check(self,days,weights,cap):

        d=1
        load=0

        for w in weights:
            if load+w>cap:
                d+=1
                load=w
            else:
                load+=w
        return d<=days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            if self.check(days,weights,mid):
                high=mid
            else:
                low=mid+1
        return low


        