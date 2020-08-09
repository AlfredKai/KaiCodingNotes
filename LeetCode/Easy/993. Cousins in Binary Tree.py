from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root == None:
            return False
        x_depth = 0
        x_p = -1
        y_depth = 0
        y_p = -1
        def DFS(root, depth, p):
            if root == None:
                return
            if root.val == x:
                nonlocal x_depth, x_p 
                x_depth = depth
                x_p = p
            if root.val == y:
                nonlocal y_depth, y_p
                y_depth = depth
                y_p = p
            DFS(root.right, depth+1, root.val)
            DFS(root.left, depth+1, root.val)
        DFS(root, 0, root.val)
        return x_depth == y_depth and x_p != y_p

a = Solution()
b = TreeNode(1)
b.left = TreeNode(2)
b.right = TreeNode(3)
b.left.left = TreeNode(4)
print(a.isCousins(b, 3, 4))
b = TreeNode(1)
b.left = TreeNode(2)
b.right = TreeNode(3)
b.left.right = TreeNode(4)
print(a.isCousins(b, 2, 3))