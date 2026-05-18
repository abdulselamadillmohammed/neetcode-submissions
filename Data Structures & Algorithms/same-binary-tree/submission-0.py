# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False

        queue1 = [p]
        queue2 = [q]
        res1 = [] 
        res2 = [] 

        while queue1:
            node = queue1.pop()
            if not node:
                res1.append("NULL")
                continue
            res1.append(node.val)
            queue1.append(node.left)
            queue1.append(node.right)

        while queue2:
            node = queue2.pop()
            if not node:
                res2.append("NULL")
                continue
            res2.append(node.val)
            queue2.append(node.left)
            queue2.append(node.right)
        print(res1,res2)
        return res1 == res2





