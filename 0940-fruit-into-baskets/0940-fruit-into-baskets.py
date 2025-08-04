from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        left = 0
        right = 0
        maxi = 0
        max_ele = float('-inf')
        
        while right < len(fruits):
            d[fruits[right]] += 1
            maxi += 1
            
            # If we have more than 2 types, shrink the window
            while len(d) > 2:
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    del d[fruits[left]]
                left += 1
                maxi -= 1

            max_ele = max(max_ele, maxi)
            right += 1  # Missing increment that caused an infinite loop
        
        return max_ele
