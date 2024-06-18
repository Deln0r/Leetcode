class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(profit, difficulty), reverse=True)
        worker.sort()
        total_profit = 0

        for prof, diff in jobs:
            while worker and diff <= worker[-1]:
                total_profit += prof
                worker.pop()
            if not worker:
                break

        return total_profit