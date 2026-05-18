class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def dfs(i, remain):
            if remain == 0:
                res.append(subset[:])
                return 

            if i == len(candidates) or remain < 0:
                return  

            subset.append(candidates[i])
            dfs(i + 1, remain - candidates[i])
            subset.pop()

            # don't include
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1

            dfs(i + 1, remain)

        dfs(0, target)
        return res
