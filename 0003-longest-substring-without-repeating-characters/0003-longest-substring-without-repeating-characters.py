from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        c=0
        maxans=0
        d=defaultdict(int)
        while r<len(s):
            d[s[r]]+=1
            while d[s[r]]>1 :
                d[s[l]]-=1
                c-=1
                l+=1
            c+=1  
            r+=1
            maxans=max(c,maxans)
        return maxans
            
