class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        d1 = {ch: 1 for ch in 'qwertyuiop'}
        d2 = {ch: 1 for ch in 'asdfghjkl'}
        d3 = {ch: 1 for ch in 'zxcvbnm'}
        res = []

        for word in words:
            c = 0
            for char in word.lower():  # convert to lowercase
                if (c == 0 or c == 1) and char in d1:
                    c = 1
                elif (c == 0 or c == 2) and char in d2:
                    c = 2
                elif (c == 0 or c == 3) and char in d3:
                    c = 3
                else:
                    c = 4
                    break
            if c != 4:
                res.append(word)
        return res
