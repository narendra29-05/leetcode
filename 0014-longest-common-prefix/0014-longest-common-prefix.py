class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans=strs[0] #----->flower
        final_ans=""
        for string in strs[1:]:
            dup=string  #--flight
            if len(string)>=len(ans):  
                dup=ans
            final_ans=""
            for i in range(len(dup)):
                if string[i]==ans[i]:
                    final_ans+=string[i]
                else:
                    break
            print(final_ans)
            ans=final_ans  #--->flow
        return ans



