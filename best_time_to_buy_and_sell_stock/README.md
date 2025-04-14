# Best Time to Buy and Sell Stock

## Problem Description

[LeetCode - Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

### Examples:

**Example 1:**
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2:**
```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done, and the max profit = 0.
```

### Constraints:

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

## Solution

The core idea is to iterate through the prices once. We keep track of the minimum price encountered so far (`min_price`) and calculate the maximum profit (`max_profit`) we could make by selling at the current price.

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            # Is this price lower than the lowest we've seen?
            min_price = min(min_price, price)
            # What's the profit if we sell today?
            profit = price - min_price
            # Is this profit the best we've seen?
            max_profit = max(max_profit, profit)
        return max_profit
```

- **Time Complexity:** O(n) - We just loop through the prices once.
- **Space Complexity:** O(1) - We only need a couple of variables. 