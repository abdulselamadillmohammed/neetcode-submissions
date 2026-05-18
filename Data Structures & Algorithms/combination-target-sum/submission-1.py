class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(i):
            if sum(subset) == target:
                res.append(subset[:])
                return
            if i >= len(nums) or sum(subset) > target:
                return

            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j)
                subset.pop()

        dfs(0)

        return res