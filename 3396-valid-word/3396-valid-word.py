class Solution:
    def isValid(self, word: str) -> bool:
        word=word.lower()
        vowels=["a","e","i","o","u"]
        cons="bcdfghjklmnpqrstvwxyz"
        numbers="1234567890"
        if len(word)<3:
            return False
        o=v=c=0
        word_list=list(set(list(word)))
        print(word_list)
        for i in word_list:
            if i in vowels:
                o=1
            elif i in cons:
                c=1
            elif i not in numbers:
                v=1
        if v:
            return False
        if (c+o)==2 and len(word)>2:
            return True
        return False
            


        