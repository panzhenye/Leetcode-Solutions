# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == root.left.val + root.right.val:
            return True
        else:
            return False


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(6)
    root.right = TreeNode(4)
    s = Solution()
    print(s.checkTree(root))
    
