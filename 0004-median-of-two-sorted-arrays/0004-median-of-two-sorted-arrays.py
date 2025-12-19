class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):
            nums1,nums2=nums2,nums1
        
        n,m=len(nums1),len(nums2)
        low,high=0,n
        while low<=high:
            topcut=(low+high)//2
            remaincut=(n+m+1)//2-topcut

            l1=float("-inf") if topcut==0 else nums1[topcut-1]

              #eddge case for handling for left most element handle underflow

            r1=float("inf") if topcut==n else nums1[topcut]

            #edge case for right element in nums1 [1,2,3,4,5,6 | (no element )] may overflow foer handling that we using edge case of topcut==n


            l2=float("-inf") if remaincut== 0 else nums2[remaincut-1]

            r2=float("inf") if remaincut == m else nums2[remaincut]

            if l1<=r2 and l2<=r1:  # chacking all are in order 
                if (n+m)%2==0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
            elif l2>r1:
                low=topcut+1
            else:
                high=topcut-1






