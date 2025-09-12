class Solution:
    def sortVowels(self, s: str) -> str:

        l=[]
        vowels="aeiouAEIOU"
        for i in s:
            if i in vowels:
                l.append(i)
        l.sort()
        j=0
        new_string=""
        for i in s:
            if i in vowels:
                new_string+=l[j]
                j+=1
            else:
                new_string+=i
        return new_string
        