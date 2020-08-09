from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        level = deque([root])
        all_level = []
        while level:
            level_vals = []
            for n in level:
                level_vals.append(n.val)
            all_level.append(level_vals)
            this_level = deque()
            while level:
                node = level.popleft()
                if node.left:
                    this_level.append(node.left)
                if node.right:
                    this_level.append(node.right)
            
            level = this_level
        return all_level[::-1]