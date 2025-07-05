class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c=Counter(arr)
        max_i=-1
        for i,j in c.items():
            if i==j:
                max_i=max(max_i,i)
        return max_i