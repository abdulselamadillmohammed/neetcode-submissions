class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        visit, cycle = set(), set()
        output = []

        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle: 
                return False
            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return []
        return output
