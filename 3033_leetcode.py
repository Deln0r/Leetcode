class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        for c in range(cols):
            max_in_col = max(matrix[r][c] for r in range(rows) if matrix[r][c] != -1)
            for r in range(rows):
                if matrix[r][c] == -1:
                    matrix[r][c] = max_in_col
        return matrix
