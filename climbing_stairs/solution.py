class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1:1, 2:2}

        def f(n):
            if n in cache:
                return cache[n]
            else:
                cache[n] = f(n-1) + f(n-2)
                return cache[n]

        return f(n) 