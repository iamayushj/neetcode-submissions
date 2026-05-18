# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
 #       5
 #      / \
 #     3   7
 #    / \
 #   2   4
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0
        self.answer = None
        def dfs(root, k):
            if not root:
                return
            dfs(root.left, k)
            self.counter += 1
            if self.counter == k:
                self.answer = root.val
                return
            dfs(root.right, k)
            
        dfs(root, k)
        return self.answer