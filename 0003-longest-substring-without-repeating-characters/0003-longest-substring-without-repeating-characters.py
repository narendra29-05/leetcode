from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        d=defaultdict(int)
        r=0
        c=0
        max_ans=float('-inf')
        while r<len(s):
            d[s[r]]+=1
            while d[s[r]]>1:
                d[s[l]]-=1
                l+=1
                c-=1
            r+=1
            c+=1
            max_ans=max(c,max_ans)
        max_ans=max(c,max_ans)
        return max_ans
            
