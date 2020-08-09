# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        path = []
        depth = 0
        def traversal(root):
            path.append(root)
            nonlocal depth
            if len(path) > depth:
                depth = len(path)
            if root.left != None:
                traversal(root.left)
            if root.right != None:
                traversal(root.right)
            path.pop()
            return
        traversal(root)
        return depth

# [3,9,20,null,null,15,7]
r = TreeNode(3)
r.left = TreeNode(9)
r.right = TreeNode(20)
r.right.left = TreeNode(15) 
r.right.right = TreeNode(7)

a = Solution()
print(a.maxDepth(r))