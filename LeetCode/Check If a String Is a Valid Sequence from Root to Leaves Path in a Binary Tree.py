from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        stack = []
        + = False
        def DFS(root):
            nonlocal found
            stack.append(root.val)
            if len(stack) <= len(arr):
                if stack[len(stack)-1] == arr[len(stack)-1]:
                    if root.left == None and root.right == None and len(stack) == len(arr):
                        found = True
                        return
                    if root.left != None and not found:
                        DFS(root.left)
                        stack.pop()
                    if root.right != None and not found:
                        DFS(root.right)
                        stack.pop()
        DFS(root)
        return found
        
a = Solution()
# b = TreeNode(1)
# b.left = TreeNode(2)
# b.right = TreeNode(3)
# b.left.left = TreeNode(4)
# b.left.right = TreeNode(5)
# b.right.left = TreeNode(6)
# b.right.right = TreeNode(7)
# print(a.isValidSequence(b, [1,3,6]))

# b = TreeNode(0)
# b.left = TreeNode(1)
# b.right = TreeNode(0)
# b.left.left = TreeNode(0)
# b.left.right = TreeNode(1)
# b.right.left = TreeNode(0)
# b.left.left.left = TreeNode(1)
# b.left.left.right = TreeNode(0)
# b.left.right.left = TreeNode(0)
# print(a.isValidSequence(b, [0,1,0,1]))