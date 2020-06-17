from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        for i in range(len(preorder)):
            if preorder[i] > root.val:
                break
        else:
            i = len(preorder)
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root

a = Solution()
# b = a.bstFromPreorder([8,5,1,7,10,12])
b = a.bstFromPreorder([4,2])
print('')