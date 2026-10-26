# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #if we want go in an increasing order in a BST,we have touse inorder traversal 
        count = k
        ans = 0

        def bin(node):
            nonlocal count
            nonlocal ans

            if node is None:
                return 
            bin(node.left)
            if count == 1:
                ans =node.val
            count -=1
            if count > 0:
                bin(node.right)
        bin(root)
        return ans
            