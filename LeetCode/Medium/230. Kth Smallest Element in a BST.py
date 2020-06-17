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

class Solution2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        count = 0
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                count += 1
                if count == k:
                    return root.val
                root = root.right

class Solution3:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.right
            else:
                root = stack.pop()
                print(root.val)
                root = root.left

b = TreeNode(5)
b.right = TreeNode(6)
b.left = TreeNode(3)
b.left.right = TreeNode(4)
b.left.left = TreeNode(2)
b.left.left.left = TreeNode(1)
a = Solution3()
print(a.kthSmallest(b, 3))