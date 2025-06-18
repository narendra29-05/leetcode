class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        end=3
        answer=[]
        for i in range(0,len(nums),end):
            if abs(nums[i]-nums[i+end-1])<=k:
                answer.append(nums[i:i+end])
            else:
                return []
        return answer