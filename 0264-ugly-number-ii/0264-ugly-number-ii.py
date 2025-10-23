class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap=[1]
        seen={1}
        ugly=1
        for _ in range(n):
            ugly=heapq.heappop(heap)
            for i in [2,3,5]:
                new_ugly=ugly*i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap,new_ugly)
        return ugly