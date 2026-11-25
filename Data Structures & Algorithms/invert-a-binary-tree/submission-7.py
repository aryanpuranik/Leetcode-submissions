# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # if root is None:
        #     return 
        # tmp = root.left
        # root.left = root.right
        # root.right = tmp
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        if not root:
            return None
        queue = deque([root])
        while queue:
            val = queue.popleft()
            if val.left:
                queue.append(val.left)
            if val.right:
                queue.append(val.right)
            val.left,val.right = val.right,val.left
        return root

