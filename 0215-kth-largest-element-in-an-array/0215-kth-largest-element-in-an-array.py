class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    
        min_heap=nums[:k]
        heapq.heapify(min_heap)
        for i in nums[k::]:
            if min_heap[0]<i:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,i)
        return min_heap[0]