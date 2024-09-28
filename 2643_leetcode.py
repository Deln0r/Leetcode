class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0, 0]
        rows = len(mat)
        cols = len(mat[0])

        for r in range(rows):
            count = sum(mat[r][c] for c in range(cols))
            if count > ans[1]:
                ans[0], ans[1] = r, count
        return ans

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0,0]
        for i, row in enumerate(mat):
            one_count = row.count(1)
            if one_count>ans[1]:
                ans[0] = i
                ans[1] = one_count
        return ans