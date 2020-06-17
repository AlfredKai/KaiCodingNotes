# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        r = [0]
        def inorder(root, dic, odd, r):
            if not root:
                return
            if root.val in dic:
                dic[root.val] += 1
                if dic[root.val] % 2 == 0:
                    odd -= 1
                else:
                    odd += 1
            else:
                dic[root.val] = 1
                odd += 1
            inorder(root.left, dic.copy(), odd, r)
            inorder(root.right, dic.copy(), odd, r)
            if not root.left and not root.right:
                if odd <= 1:
                    r[0] += 1
        inorder(root, {}, 0, r)
        return r[0]