# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        level = [(root, 0)]
        r = 0
        while level:
            next_level = []
            cur_min = level[0][1]
            cur_max = level[0][1]
            for node, index in level:
                if node.left:
                    next_level.append((node.left, index*2))
                if node.right:
                    next_level.append((node.right, index*2+1))
            cur_min = min(cur_min, index)
            cur_max = max(cur_max, index)
            r = max(r, cur_max - cur_min + 1)
            level = next_level
        return r