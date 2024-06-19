class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def helper(day: int)-> bool:

            s = ''.join(['X' if b <= day else
                                     ' ' for b in bloomDay])
            return s.count('X'*k) >= m


        n, mn, mx = len(bloomDay), min(bloomDay), max(bloomDay)+1
        if n < m * k: return -1

        return mn + bisect_left(range(mn, mx), True, key = helper)