class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removal(s,first,second,points):
            score=0
            stack=[]
            for ch in s:
                if stack and stack[-1]==first and ch==second :
                    score+=points
                    stack.pop()
                    continue
                stack.append(ch)
            return "".join(stack),score
        
        if x>y:
            remaing_string,score1=removal(s,"a","b",x)
            _,score2=removal(remaing_string,"b","a",y)
        else:
            remaing_string,score2=removal(s,"b","a",y)
            _,score1=removal(remaing_string,"a","b",x)
        return score1+score2