# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        q = deque()
        res = []
        q.append(root)

        while q:
            rightval = None
            level = len(q)
            for i in range(level):
                node = q.popleft()
                if node:
                    rightval = node
                    q.append(node.left)
                    q.append(node.right)
                
            if rightval:
                res.append(rightval.val)
        return res
            
            



