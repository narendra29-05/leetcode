class Solution:
    def fib(self, n: int) -> int:
        d=[0]*(n+1)
        def feb(n,d):
            if n<=1:
                return n
            if d[n]:
                return d[n]
            d[n]=(feb(n-1,d)+feb(n-2,d))
            return d[n]
        return feb(n,d)
