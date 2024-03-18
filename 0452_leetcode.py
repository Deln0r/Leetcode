class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        min_end, cnt = -inf, 0
        for start, end in sorted(points, key=itemgetter(1)):
            if min_end < start:
                min_end = end
                cnt += 1
        return cnt