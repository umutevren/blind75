# Two Sum

## Problem Description

[LeetCode - Two Sum](https://leetcode.com/problems/two-sum/)

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Examples:

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Constraints:

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

## Solution Approach

The solution uses a hash map to store previously seen numbers and their indices. For each number in the array:

1. Calculate the complement (target - current number)
2. Check if the complement exists in the hash map
3. If it does, return the indices of both the complement and the current number
4. If not, add the current number and its index to the hash map

This approach has:
- Time Complexity: O(n) where n is the length of the array
- Space Complexity: O(n) for storing the hash map

## Code Explanation

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
```

This is an elegant one-pass hash table solution. As we iterate through the array, we're simultaneously looking for the complement and building our hash map of number-to-index mappings. 