class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        visitSet = set()
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if preMap[crs] == []:
                return True
            if crs in visitSet:
                return False
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True