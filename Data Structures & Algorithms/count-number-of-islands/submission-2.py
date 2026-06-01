class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        islands, visit = 0, set()
        q = collections.deque()
        directions = [[1,0], [0,1], [0,-1],[-1,0]]

        def bfs():
            while q:
                row,col = q.popleft()
                for dr, dc in directions:
                    r,c= row + dr, col + dc 
                    if (r in range(ROWS) and c in range(COLS) and (r,c) not in visit and grid[r][c] == "1"):
                        q.append((r,c)) 
                        visit.add((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == "1":
                    q.append((r,c))
                    bfs()
                    islands += 1
        return islands