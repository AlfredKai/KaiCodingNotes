# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True

        def traversal(root):
            if root.left != None:
                leftMinMax = traversal(root.left)
            if root.right != None:
                rightMinMax = traversal(root.right)
            if leftMinMax[1]

            return [leftMinMax[1], rightMinMax[0]]
        traversal(root)
        return r

r = TreeNode(5)
r.left = TreeNode(1)
r.right = TreeNode(4)
r.right.left = TreeNode(3)
r.right.right = TreeNode(6)

a = Solution()
print(a.isValidBST(r))