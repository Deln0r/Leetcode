class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        c1 = 0
        c2 = n -1

        for r in range(n):
            ans += mat[r][c1]
            c1 += 1
            if r != c2:
                ans += mat[r][c2]
            c2 -= 1

        return ans