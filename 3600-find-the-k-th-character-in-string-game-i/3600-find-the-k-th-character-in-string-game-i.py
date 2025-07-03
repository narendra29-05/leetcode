class Solution:
    def kthCharacter(self, k: int) -> str:
        
        k-=1
        c=0
        while k:
            if k & 1:
                c+=1
            k>>=1
        return chr(ord("a")+c)
        