class Solution:
    def kthCharacter(self, k: int) -> str:
        stack=["a"]
        i=0
        while i<k:
            n=len(stack)
            j=0
            while i<k and j< n :
                char=stack[j]
                if char=="z":
                    stack.append("a")
                    j+=1
                    continue
                stack.append(chr(ord(char) + 1))
                j+=1

                i+=1
        print(stack)

        return stack[k-1]
            
