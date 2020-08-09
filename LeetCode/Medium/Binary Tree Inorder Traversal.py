from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

a = Solution()
r = TreeNode(1) # [1,null,2,3]
r.right = TreeNode(2)
r.right.left = TreeNode(3)
print(a.inorderTraversal(r)) # expected: [1,3,2]

class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        a = []
        a.append(root)
        r = []
        while len(a) > 0:
            b = a.pop()
            if b.right:
                a.append(b.right)
            if b.left:
                a.append(TreeNode(b.val))
                a.append(b.left)
            else:
                r.append(b.val)
        return r

a = Solution2()
r = TreeNode(1) # [1,null,2,3]
r.right = TreeNode(2)
r.right.left = TreeNode(3)
print(a.inorderTraversal(r))
assert a.inorderTraversal(r) == [1,3,2]

r = TreeNode(1) # [1,2,3,4,5,6,7]
r.left = TreeNode(2)
r.right = TreeNode(3)
r.left.left = TreeNode(4)
r.left.right = TreeNode(5)
r.right.left = TreeNode(6)
r.right.right = TreeNode(7)
print(a.inorderTraversal(r))
assert a.inorderTraversal(r) == [4,2,5,1,6,3,7]

r = TreeNode(2) # [2,3,null,1]
r.left = TreeNode(3)
r.left.left = TreeNode(1)
print(a.inorderTraversal(r))
assert a.inorderTraversal(r) == [1,3,2]

r = TreeNode(3) # [3,1,null,null,2]
r.left = TreeNode(1)
r.left.right = TreeNode(2)
print(a.inorderTraversal(r))
assert a.inorderTraversal(r) == [1,2,3]