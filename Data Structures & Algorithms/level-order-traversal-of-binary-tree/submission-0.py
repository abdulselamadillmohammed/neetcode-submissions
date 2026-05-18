# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append([root, 0])
        output = []
        while q:
            node, height = q.popleft() 
            if not node:
                continue
            if (len(output) - 1) < height:
                output.append([])
            output[-1].append(node.val)
            q.append([node.left, height + 1])
            q.append([node.right, height + 1])

        return output