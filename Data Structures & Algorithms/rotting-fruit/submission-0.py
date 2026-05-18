class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0,0
        directions = [[0,1] , [0,-1] , [1,0] , [-1,0]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    q.append((r,c))

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for row, col in directions:
                    if (row + r < 0 or row + r == ROWS or 
                    col + c < 0 or col + c == COLS or grid[row + r][col + c] != 1):
                        continue

                    grid[row + r][col + c] = 2
                    q.append((row + r, col + c))
                    fresh-=1
            time +=1
        return time if fresh == 0 else -1