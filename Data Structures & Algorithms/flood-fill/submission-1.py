class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        col = image[sr][sc]
        visited = set()
        def dfs(sr, sc):
            if (sr < 0 or sr == ROWS or sc < 0 or sc == COLS or image[sr][sc] != col or (sr,sc) in visited):
                return 

            image[sr][sc] = color

            visited.add((sr,sc))
            dfs(sr+1,sc)
            dfs(sr-1,sc)
            dfs(sr,sc+1)
            dfs(sr,sc-1)
            visited.remove((sr,sc))


        dfs(sr,sc)
        return image