class Solution:
    def climbStairs(self, n: int) -> int:
        hashMap = {}
        def dfs(num):
            if num > n:
                return 0
            if num == n:
                return 1

            if hashMap.get(num):
                return hashMap[num]
            hashMap[num] = dfs(num + 1) + dfs(num + 2)
            return hashMap[num]

        hashMap[0] = dfs(0)
        return hashMap[0]