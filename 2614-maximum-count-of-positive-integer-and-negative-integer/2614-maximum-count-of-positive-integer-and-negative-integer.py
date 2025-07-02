from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        # Find the first positive number index
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1
        positive = n - left  # elements after 'left' are positive

        # Find the last negative number index
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1
        negative = right + 1  # elements before 'right' are negative

        return max(positive, negative)
