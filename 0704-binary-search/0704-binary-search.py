class Solution:
    def search(self, nums, target) :
        for i,element in enumerate(nums):
            if target==element:
                return i 
        return -1