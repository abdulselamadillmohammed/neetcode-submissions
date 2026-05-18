class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        dic = {}
        def dfs(n):
            if n < 0:
                return 0 
            if n == 0:
                return 1
            if dic.get(n):
                return dic[n]
            dic[n] = dfs(n-1) + dfs(n-2)
            return dic[n]

        
        dfs(n)
        return dic[n]