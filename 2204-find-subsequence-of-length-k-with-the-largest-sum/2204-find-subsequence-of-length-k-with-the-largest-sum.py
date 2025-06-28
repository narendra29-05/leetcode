class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        dummy=nums.copy()
        dummy.sort(reverse=True)
        counter=Counter(dummy[:k])
        print(counter)
        answer=[]
        print()
        for i in nums:
            if len(answer)==k:
                break
            if counter[i]:
                answer.append(i)
                counter[i]-=1
        return answer