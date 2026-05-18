class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)
        perm = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return 
            
            for i in count:
                if count[i] > 0:
                    count[i] -= 1
                    perm.append(i)
                    dfs()
                    count[i] += 1
                    perm.pop()

        dfs()

        return res