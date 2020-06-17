from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        result = []
        nextLevel = []
        nextLevel.append(root)
        order = -1
        while len(nextLevel) != 0:
            temp = []
            level = []
            for node in nextLevel:
                level.append(node.val)
                if node.left != None:
                    temp.append(node.left)
                if node.right != None:
                    temp.append(node.right)
            order = -order
            result.append(level[::order])
            nextLevel = temp
        return result

b = TreeNode(3)
b.left = TreeNode(9)
b.right = TreeNode(20)
b.right.left = TreeNode(15)
b.right.right = TreeNode(7)
a = Solution()
print(a.zigzagLevelOrder(b))