1044. Longest Duplicate Substring
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import math
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(root):
            if root == None:
                return (-math.inf, -math.inf)
            if root.left == None and root.right == None:
                return (root.val, -math.inf)
            left = helper(root.left)
            right = helper(root.right)
            noRootMaxSum = max(left[0], left[1], right[0], right[1], root.val+left[0]+right[0])
            rootMax = max(root.val, root.val+left[0], root.val+right[0])
            return (rootMax, noRootMaxSum)

        return max(helper(root))

a = Solution()
b = TreeNode(1)
b.left = TreeNode(2)
b.right = TreeNode(3)
print(a.maxPathSum(b))
b = TreeNode(-10)
b.left = TreeNode(9)
b.right = TreeNode(20)
b.right.left = TreeNode(15)
b.right.right = TreeNode(7)
print(a.maxPathSum(b))
b = TreeNode(-3)
print(a.maxPathSum(b))
b = TreeNode(5)
b.left = TreeNode(4)
b.right = TreeNode(8)
b.left.left = TreeNode(11)
b.right.left = TreeNode(13)
b.right.right = TreeNode(4)
b.left.left.left = TreeNode(7)
b.left.left.right = TreeNode(2)
b.right.right.right = TreeNode(1)
print(a.maxPathSum(b))