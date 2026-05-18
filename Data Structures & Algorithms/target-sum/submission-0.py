class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(index, suum):
            if index == len(nums):
                return 1 if suum == target else 0

            if (index, suum) in dp:
                return dp[(index, suum)]

            dp[(index, suum)] = dfs(index + 1, suum + nums[index]) + dfs(index + 1, suum - nums[index])
            return dp[(index, suum)]

        return dfs(0, 0)
