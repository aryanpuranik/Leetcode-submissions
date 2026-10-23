# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def binary(node,left,right):
            if node is None:
                return True
            if not(node.val<right and node.val>left):
                return False
            left = binary(node.left,left,node.val)
            right = binary(node.right,node.val,right)

            if left is True and right is True:
                return True
            else:
                return False
        return binary(root, float('-inf'),float('inf'))