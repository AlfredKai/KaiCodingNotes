# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        def x(root, innerPre, innerIn):
            if len(innerPre) == 0:
                return None
            if len(innerPre) == 1:
                return TreeNode(innerPre[0])

            rootInorder = innerIn.index(root.val)

            preLeft = innerPre[1:rootInorder+1]
            preRight = innerPre[rootInorder+1:]

            inLeft = innerIn[0:rootInorder]
            inRight = innerIn[rootInorder+1:]

            if len(preLeft) > 0:
                root.left = x(TreeNode(preLeft[0]), preLeft, inLeft)
            if len(preRight) > 0:
                root.right = x(TreeNode(preRight[0]), preRight, inRight)
            return root
        
        return x(TreeNode(preorder[0]), preorder, inorder)

a = Solution()
a.buildTree([3,9,20,15,7], [9,3,15,20,7])
