class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def row_zero(i,j):
            for k in range(len(matrix[0])):
                if matrix[i][k] != "T":
                    matrix[i][k] = 0

            for z in range(len(matrix)):
                if matrix[z][j] != "T":
                    matrix[z][j] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = "T"

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "T":
                    row_zero(i,j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "T":
                    matrix[i][j] = 0