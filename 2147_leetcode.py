class Solution:
  def numberOfWays(self, s: str) -> int:
    res, mod, num_seats, s, num_gap = 1, 10**9 + 7, 0, s.strip('P'), 1
    for c in s:
      if c == 'S':
        res, num_seats, num_gap = (res * num_gap) % mod, num_seats + 1, 1
      elif num_seats % 2 == 0:
        num_gap += 1
    
    return 0 if num_seats % 2 or not num_seats else res
