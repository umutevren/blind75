from typing import List

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