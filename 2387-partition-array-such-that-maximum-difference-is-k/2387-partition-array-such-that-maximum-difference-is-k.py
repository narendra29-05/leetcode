class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        answer = 1
        rec = nums[0]
        for num in nums:
            if num - rec > k:
                answer += 1
                rec = num
        return answer