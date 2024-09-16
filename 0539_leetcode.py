class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        vect = []
        for t in timePoints:
            h, m = map(int, t.split(':'))
            vect.append(h*60+m)
        vect.sort()

        ans = 1441
        for i in range(1, len(vect)):
            ans = min(vect[i] - vect[i-1], ans)

        return min(ans, vect[0] - vect[-1] + 1440)