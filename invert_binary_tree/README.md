# Invert Binary Tree

[LeetCode - Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

Given the root of a binary tree, invert the tree, and return its root.

### Solution

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = right, left

        return root
```

- **Time Complexity:** O(n) where n is the number of nodes in the tree
- **Space Complexity:** O(h) where h is the height of the tree (due to recursion stack) 