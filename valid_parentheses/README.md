# Valid Parentheses

[LeetCode - Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

### Examples:

```
Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
```

### Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in brackets_map.values():
                stack.append(char)
            elif char in brackets_map:
                if not stack or stack.pop() != brackets_map[char]:
                    return False  

        return len(stack) == 0
```

- **Time Complexity:** O(n)
- **Space Complexity:** O(n) 