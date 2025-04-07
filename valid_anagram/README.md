# Valid Anagram

## Problem Description

[LeetCode - Valid Anagram](https://leetcode.com/problems/valid-anagram/)

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Examples:

**Example 1:**
```
Input: s = "anagram", t = "nagaram"
Output: true
```

**Example 2:**
```
Input: s = "rat", t = "car"
Output: false
```

### Constraints:

- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

## Solution Approach

The solution first converts both strings to lowercase and then sorts them to check if they are equal. If both sorted strings are identical, they contain the same characters with the same frequencies, which means they are anagrams.

This approach has:
- Time Complexity: O(n log n) where n is the length of the string (due to sorting)
- Space Complexity: O(n) to store the sorted strings

## Code Explanation

```python
def isAnagram(self, s: str, t: str) -> bool:
    s = s.lower()
    t = t.lower()
    
    if sorted(s) == sorted(t):
        return True
    else:
        return False
```

The solution could be further simplified to:
```python
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s.lower()) == sorted(t.lower())
``` 