class Solution:
  def countUnguarded(self, m: int, n: int, G: List[List[int]], W: List[List[int]]) -> int:
    D = [[0]*n for _ in range(m)]
    for r, c in G + W:
      D[r][c] = 1 # obstacle

    dirs = [(0,1),(1,0),(-1,0),(0,-1)]
    for row, col in G:
      for dr, dc in dirs:
        r, c = row, col
        while 0 <= r+dr < m and 0 <= c + dc < n and D[r+dr][c+dc] != 1:
          r, c = r+dr, c+dc
          D[r][c] = 2 # viewed

    return sum(row.count(0) for row in D)
        