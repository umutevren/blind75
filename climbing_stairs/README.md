# Climbing Stairs

[LeetCode - Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

### Solution

```python
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
```

- **Time Complexity:** O(n)
- **Space Complexity:** O(n) 