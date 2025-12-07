class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=set(nums1)
        n2=list(set(nums2))
        new=[]
        for i in n1:
            if i in n2:
                new.append(i)
        return new