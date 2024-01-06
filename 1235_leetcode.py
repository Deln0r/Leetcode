class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort()
        jobs.append((maxsize, 0, 0))

        maxProfit, h = 0, []
        for s, e, p in jobs:
            while h and h[0][0] <= s:
                maxProfit = max(maxProfit, heappop(h)[1])

            heappush(h, (e, maxProfit + p))

        return maxProfit
