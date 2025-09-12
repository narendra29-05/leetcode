class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels="aaeiou"
        vowel=0
        for i in s:
            if i in vowels:
                vowel+=1
        if vowel >=1:
            return True
        return False
        