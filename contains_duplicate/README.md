# Contains Duplicate

## Problem Description

[LeetCode - Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

### Examples:

**Example 1:**
```
Input: nums = [1,2,3,1]
Output: true
```

**Example 2:**
```
Input: nums = [1,2,3,4]
Output: false
```

**Example 3:**
```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

### Constraints:

- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

## Solution Approach

The solution uses Python's built-in `set` data structure to remove duplicates. By comparing the length of the original array with the length of the set created from the array, we can determine if duplicates exist:

- If the lengths are equal, there are no duplicates (returns `False`)
- If the lengths are different, there are duplicates (returns `True`)

This approach has:
- Time Complexity: O(n) where n is the length of the array
- Space Complexity: O(n) for storing the set

## Code Explanation

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
```

The solution converts the input array to a set, which automatically removes duplicates. Then it compares the length of the original array with the length of the set. If they differ, duplicates were present in the original array. 