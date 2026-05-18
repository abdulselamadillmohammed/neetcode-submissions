# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                continue
            output.append(node.val)
            q.append(node.left)
            q.append(node.right)

        import heapq

        heapq.heapify(output)
        k -= 1
        while output:
            val = heapq.heappop(output)
            if k == 0:
                return val
            k -= 1

        return -1
        

