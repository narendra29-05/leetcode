class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans=0
        final=0
        ans_index=-1
        for i in range (len(customers)):
            if customers[i]=="Y":
                ans+=1
            else:
                ans+=-1
            if final<ans:
                final=ans
                ans_index=i
        return ans_index+1

