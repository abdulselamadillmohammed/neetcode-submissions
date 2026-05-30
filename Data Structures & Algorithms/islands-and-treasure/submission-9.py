class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q, visit = deque(), set()
        ROWS, COLS = len(grid), len(grid[0])

        def addRoom(r,c):
            if (r == ROWS or r < 0 or c == COLS or c < 0 or (r,c) in visit or grid[r][c] == -1):
                return
            q.append((r,c))
            visit.add((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                visit.add((row, col))
                grid[row][col] = dist

                addRoom(row + 1, col)
                addRoom(row - 1, col)
                addRoom(row, col + 1)
                addRoom(row, col - 1)

            dist += 1



