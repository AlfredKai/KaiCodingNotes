# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        r = [0]
        def DFS(node: TreeNode, depth: int) -> int:
            if not node.left and not node.right:
                return [depth]
            left_leaves = DFS(node.left, depth+1) if node.left else []
            right_leaves = DFS(node.right, depth+1) if node.right else []
            for d in left_leaves:
                for d2 in right_leaves:
                    if d + d2 - 2 * depth<= distance:
                        r[0] += 1
            return left_leaves + right_leaves

        DFS(root, 0)
        return r[0]
