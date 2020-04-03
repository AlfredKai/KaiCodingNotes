# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        rlist = []
        def traversal(r):
            if r == None:
                return
            if r.left != None:
                traversal(r.left)
            # print(r.val)
            rlist.append(r.val)
            if r.right != None:
                traversal(r.right)
        traversal(root)
        return rlist[k-1]

b = TreeNode(5)
b.right = TreeNode(6)
b.left = TreeNode(3)
b.left.right = TreeNode(4)
b.left.left = TreeNode(2)
b.left.left.left = TreeNode(1)
a = Solution()
print(a.kthSmallest(b, 3))