class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n, sum = len(matrix), len(matrix[0]), 0

        cons1s = [0] * n
        for i in range(m):
            for j in range(n):
                cons1s[j] = cons1s[j] + 1 if matrix[i][j] != 0 else 0
            sorted1s = sorted (cons1s, reverse = True)
            for j in range(n):
                sum = max(sum, (j + 1) * sorted1s[j])

        return sum
