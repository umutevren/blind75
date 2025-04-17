# Reverse Linked List

[LeetCode - Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

Given the head of a singly linked list, reverse the list, and return the reversed list.

### Solution

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_one = curr.next
            curr.next = prev
            prev = curr
            curr = next_one
        return prev
```

- **Time Complexity:** O(n)
- **Space Complexity:** O(1) 